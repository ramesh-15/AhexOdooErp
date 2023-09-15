{
    "name": "School ERP",
    'author': 'Ahex Technology',
    'version': '1.0.0',
    'category': 'Administration/School',
    'description': """
                Ahex School management tool is here now.""",
    'data': [
        "security/ir.model.access.csv",
        'views/menu.xml',
        'views/student.xml',
        'views/staff.xml',
        'views/subject.xml',
        'views/syllabus.xml',
        'views/fee.xml',
    ],

    'web.assets_backend': [
        'static/src/css/admission_tree_views.scss',
    ],
}
