from playwright.sync_api import sync_playwright
import os

def run(playwright):
    browser = playwright.chromium.launch()
    page = browser.new_page()

    # Verify signup
    signup_path = os.path.abspath("lectural signup.html")
    page.goto(f"file://{signup_path}")
    page.fill("#schoolEmail", "testuser@example.com")
    page.fill("#password", "password123")
    page.click("#signupBtn")
    page.wait_for_url("**/lecturals_Dashboard.html")
    page.screenshot(path="jules-scratch/verification/lecturer_dashboard.png")

    # Verify signin
    signin_path = os.path.abspath("student_signin.html")
    page.goto(f"file://{signin_path}")
    page.fill("#loginEmail", "testuser@example.com")
    page.fill("#loginPassword", "password123")
    page.click("#loginBtn")
    page.wait_for_url("**/stdent_dashbord.html")
    page.screenshot(path="jules-scratch/verification/student_dashboard.png")

    browser.close()

with sync_playwright() as playwright:
    run(playwright)
