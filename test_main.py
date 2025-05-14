import os
import pandas as pd
from main import load_users, sort_users, generate_html_report

def test_load_users_valid_csv():
    df = load_users("users.csv")
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert all(col in df.columns for col in ['name', 'surname', 'age', 'group'])

def test_sort_users_by_name():
    df = load_users("users.csv")
    sorted_df = sort_users(df, "name")
    assert sorted_df.iloc[0]["name"] <= sorted_df.iloc[1]["name"]

def test_generate_html_report_creates_file(tmp_path):
    df = load_users("users.csv")
    template_content = """
    <html><body>
    {% for user in users %}
        <p>{{ user.name }} {{ user.surname }}</p>
    {% endfor %}
    </body></html>
    """
    # Scriem template-ul în directorul curent pentru a fi vizibil pentru FileSystemLoader('.')
    template_file = "test_template.html"
    with open(template_file, "w", encoding="utf-8") as f:
        f.write(template_content)

    output_file = tmp_path / "output.html"
    try:
        generate_html_report(df, template_file, str(output_file))
        assert output_file.exists()
    finally:
        os.remove(template_file)

