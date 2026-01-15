run_set = [
    'Behave/features/current_regression/cms/cms_admin_page_ui.feature',
    'Behave/features/current_regression/cms/cms_access_permission.feature',
    'Behave/features/current_regression/pub/forward_article.feature:25'  # Specific scenario
]

# print(run_set)
print("========== LIST ENUMERATE ==========")
for i, scenario in enumerate(run_set):
    print(scenario)