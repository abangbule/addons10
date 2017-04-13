{
	"name": "Academic Information System Day",
	"version": "1.0", 
	"depends": [
		"base",
		"account",
		"sale",
		"board",
	],
	"author": "gian.ule@gmail.com", 
	"category": "Education", 
	'website': 'http://www.vitraining.com',
	"description": """\
Academic Information System Day 1


""",
	"data": [
		"menu.xml",
		"course.xml",
		"session.xml",
		"attendee.xml",
		"partner.xml",
		"workflow.xml",
		"security/group.xml",
		"security/ir.model.access.csv",
		"wizard/create_attendee.xml",
		"dashboard.xml",
		"report/session.xml",
	],
	"installable": True,
	"auto_install": False,
    "application": True,
}
