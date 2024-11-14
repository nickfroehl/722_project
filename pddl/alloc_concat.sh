#!/bin/bash

# Top-level directory containing <domain>.pddl files and subdirectories
TOP_DIR="${1:-.}"

# Loop through each <domain>.pddl file in the top-level directory
for domain_file in "$TOP_DIR"/*.pddl; do
    # Get the base name of the domain file without extension
    domain_name=$(basename "$domain_file" .pddl)
    
    # Define the corresponding subdirectory for the domain
    domain_dir="$TOP_DIR/$domain_name"
    
    # Check if the domain directory exists and is a directory
    if [[ -d "$domain_dir" ]]; then
        # Create the combined directory inside the domain directory
        combined_dir="$domain_dir/combined"
        mkdir -p "$combined_dir"

        # Loop through each .pddl file in the domain directory
        for file in "$domain_dir"/*.pddl; do
            # Skip if no .pddl files are found
            [[ -e "$file" ]] || continue

            # Get the base name of the file without extension
            file_name=$(basename "$file" .pddl)

            # Define the output file path in the combined directory
            combined_file="$combined_dir/${file_name}_combined.pddl"

            # Concatenate <domain>.pddl and the file, and write to the combined file
            cat "$domain_file" "$file" > "$combined_file"
            echo "Created $combined_file"
        done
    else
        echo "Warning: Directory $domain_dir does not exist."
    fi
done
