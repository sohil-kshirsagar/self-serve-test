#!/bin/bash

set -e  # Exit on any error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check if git and gh are installed
if ! command -v git &> /dev/null; then
    print_error "git is not installed or not in PATH"
    exit 1
fi

if ! command -v gh &> /dev/null; then
    print_error "gh (GitHub CLI) is not installed or not in PATH"
    exit 1
fi

# Check if we're in a git repository
if ! git rev-parse --git-dir > /dev/null 2>&1; then
    print_error "Not in a git repository"
    exit 1
fi

# Get current branch
current_branch=$(git branch --show-current)
print_status "Current branch: $current_branch"

# Check if we're on main branch
if [ "$current_branch" != "main" ]; then
    print_warning "You are not on the main branch (currently on: $current_branch)"
    read -p "Do you want to continue? (y/n): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        print_status "Aborted by user"
        exit 0
    fi
fi

# Stash any changes
print_status "Stashing any uncommitted changes..."
git stash push -m "Auto-stash before creating test PR - $(date)"

# Checkout main branch and pull latest changes
print_status "Switching to main branch and pulling latest changes..."
git checkout main
git pull origin main

# Generate branch name with timestamp
current_date=$(date +%m%d%Y)
timestamp_ms=$(date +%s%3N)
branch_name="e2e-test-${current_date}-${timestamp_ms}"

print_status "Creating new branch: $branch_name"
git checkout -b "$branch_name"

# Update the file - append "EXAMPLE" to utils/string_utils.py
print_status "Updating utils/string_utils.py..."
NEW_FUNCTION_IN_STRING_UTILS="
def capitalize_last_letter(string):
    return string[:-1] + string[-1].upper()
"
echo "$NEW_FUNCTION_IN_STRING_UTILS" >> utils/string_utils.py

# Stage and commit the changes
git add utils/string_utils.py
git commit -m "Added utils"

# Push the branch
print_status "Pushing branch to origin..."
git push origin "$branch_name"

# Create PR using GitHub CLI
print_status "Creating Pull Request..."
pr_title="Added utils"

gh pr create \
    --title "$pr_title" \
    --body "Automated test PR" \
    --base main \
    --head "$branch_name"

print_status "✅ Test PR created successfully!"
print_status "Branch: $branch_name"

# Get the PR URL
pr_url=$(gh pr view --json url --jq '.url')
print_status "PR URL: $pr_url"

print_status "Script completed successfully!"
