#!/bin/bash

# Directory containing the scripts
BASE_DIR=~/\[pylon\]/pylon/src

# Whitelist and blacklist arrays
WHITELIST=()
BLACKLIST=("__init__.py","init/*","__init__")

# Alias file
ALIAS_FILE=~/.bash_aliases

# Function to convert a string to snake_case
to_snake_case() {
    echo "$1" | sed -r 's/([a-z])([A-Z])/\1_\2/g' | tr '[:upper:]' '[:lower:]' | tr -d ' '
}

# Function to generate aliases
generate_aliases() {
    local base_dir=$1
    local whitelist=("${!2}")
    local blacklist=("${!3}")

    # Create a temporary file to hold the new aliases
    local temp_file=$(mktemp)

    # Iterate through the subdirectories and files
    for subdir in "$base_dir"/*; do
        if [ -d "$subdir" ]; then
            local subdir_name=$(basename "$subdir")
            for script in "$subdir"/*.py; do
                if [ -f "$script" ]; then
                    local script_name=$(basename "$script")
                    
                    # Check if the script is in the blacklist
                    if [[ " ${blacklist[@]} " =~ " ${script_name} " ]]; then
                        continue
                    fi

                    # Check if the subdir is in the whitelist (if whitelist is not empty)
                    if [ ${#whitelist[@]} -ne 0 ] && [[ ! " ${whitelist[@]} " =~ " ${subdir_name} " ]]; then
                        continue
                    fi

                    # Convert to snake_case
                    local alias_name=$(to_snake_case "${subdir_name}_${script_name%.py}")

                    # Create the alias
                    echo "alias ${alias_name}='python3 ${script}'" >> "$temp_file"
                fi
            done
        fi
    done

    # Remove old aliases generated by this script
    sed -i '/# BEGIN PYLON ALIASES/,/# END PYLON ALIASES/d' "$ALIAS_FILE"

    # Add new aliases to the alias file
    {
        echo "# BEGIN PYLON ALIASES"
        cat "$temp_file"
        echo "# END PYLON ALIASES"
    } >> "$ALIAS_FILE"

    # Clean up the temporary file
    rm "$temp_file"
}

# Function to watch for changes and update aliases
watch_for_changes() {
    inotifywait -m -r -e create,delete,modify,move "$BASE_DIR" | while read -r; do
        generate_aliases "$BASE_DIR" WHITELIST[@] BLACKLIST[@]
        source "$ALIAS_FILE"
        echo "Aliases have been updated."
    done
}

# Generate aliases initially
generate_aliases "$BASE_DIR" WHITELIST[@] BLACKLIST[@]
source "$ALIAS_FILE"
echo "Aliases have been generated and added to $ALIAS_FILE"

# Watch for changes and update aliases
watch_for_changes
