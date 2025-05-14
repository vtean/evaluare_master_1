import pandas as pd
from jinja2 import Environment, FileSystemLoader
import argparse
import os

def load_users(csv_file):
    """Load user data from a CSV file."""
    try:
        df = pd.read_csv(csv_file)
        # Ensure required columns exist
        required_columns = ['name', 'surname', 'age', 'group']
        if not all(col in df.columns for col in required_columns):
            raise ValueError("CSV must contain 'name', 'surname', 'age', 'group' columns")
        return df
    except FileNotFoundError:
        print(f"Error: {csv_file} not found")
        exit(1)
    except Exception as e:
        print(f"Error loading CSV: {e}")
        exit(1)

def sort_users(df, sort_by):
    """Sort users by specified column."""
    if sort_by in df.columns:
        return df.sort_values(by=sort_by)
    else:
        print(f"Warning: '{sort_by}' is not a valid column. Using unsorted data.")
        return df

def display_users(df):
    """Display users in the console."""
    print("\nList of Users:")
    print("-" * 60)
    for _, row in df.iterrows():
        print(f"Name: {row['name']}")
        print(f"Surname: {row['surname']}")
        print(f"Age: {row['age']}")
        print(f"Group: {row['group']}")
        print("-" * 60)

def generate_html_report(df, template_file, output_file):
    """Generate an HTML report from user data."""
    try:
        env = Environment(loader=FileSystemLoader('.'))
        template = env.get_template(template_file)
        html_content = template.render(users=df.to_dict('records'))
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
        print(f"HTML report: {output_file}")
    except Exception as e:
        print(f"Error generating HTML report: {e}")

def main():
    parser = argparse.ArgumentParser(description="User Management Program")
    parser.add_argument('--csv', default='users.csv', help='Path to CSV file')
    parser.add_argument('--sort', default='name', help='Sort by column (name, surname, age, group)')
    parser.add_argument('--html', action='store_true', help='Generate HTML report')
    args = parser.parse_args()

    # Load and process user data
    users_df = load_users(args.csv)
    sorted_users = sort_users(users_df, args.sort)

    # Display users in console
    display_users(sorted_users)

    # Generate HTML report if requested
    if args.html:
        generate_html_report(sorted_users, 'template.html', 'users_report.html')

if __name__ == "__main__":
    main()