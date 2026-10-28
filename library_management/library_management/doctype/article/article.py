from frappe.website.website_generator import WebsiteGenerator

class Article(WebsiteGenerator):
    website = {
        "template": "library_management/doctype/article/www/article.html",
        "condition_field": "published",
        "page_title_field": "article_name",
       }
