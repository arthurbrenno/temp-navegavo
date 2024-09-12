#!/bin/bash

# Get the list of changed files
changed_files=$(git status --porcelain | awk '{print $2}')

# Loop through each changed file
for file in $changed_files
do
    # Add the file
    git add "$file"
    
    # Commit with a default message
    git commit -m "Update $file"
done

# Push to the default remote
git push
