# @author Vivek
# @version 1.0
# @since 25-07-2019

from jinja2 import Template


class HtmlGenerator:
    def __init__(self):
        pass

    def generate_html_from_template(self, core_list):
        template = Template(open('template.html').read())
        return template.render(header="Demo For Jinja", core_list=core_list)
