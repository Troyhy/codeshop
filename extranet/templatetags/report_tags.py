from django import template


register = template.Library()


@register.inclusion_tag('extranet/show_hours_report.html')
def show_hours_report(report, show_timenav=True, show_header=True,
                      show_coder_related_to_hours=False,
                      show_project_for_other_hours=True,
                      link_title_to_github=False):
    return {
        'report': report,
        'show_timenav': show_timenav,
        'show_header': show_header,
        'show_coder_related_to_hours': show_coder_related_to_hours,
        'show_project_for_other_hours':show_project_for_other_hours,
        'link_title_to_github': link_title_to_github,
    }
