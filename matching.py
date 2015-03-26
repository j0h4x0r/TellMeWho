from collections import OrderedDict

accepted_type_list = OrderedDict([
    ('/people/person', 'Person'),
    ('/people/deceased_person', 'Person'),
	('/book/author', 'Author'),
	('/film/actor', 'Actor'),
	('/tv/tv_actor', 'Actor'),
	('/organization/organization_founder', 'BusinessPerson'),
	('/business/board_member', 'BusinessPerson'),
	('/sports/sports_league', 'League'),
	('/sports/sports_team', 'SportsTeam'),
	('/sports/professional_sports_team', 'SportsTeam'),
])

information_map = OrderedDict([
	('/people/person', {
		'/type/object/name': 'Name',
		'/people/person/date_of_birth': 'Birthday',
		'/people/person/place_of_birth': 'Place of Birth',
		'/people/person/sibling_s': {
			'name': 'Siblings',
			'children': {
				'/people/sibling_relationship/sibling': 'Sibling',
			},
		},
		'/people/person/spouse_s': {
			'name': 'Spouse(s)',
			'children': {
				'/people/marriage/spouse': 'Spouse Name',
				'/people/marriage/from': 'Marriage From',
				'/people/marriage/to': 'Marriage To',
				'/people/marriage/location_of_ceremony': 'Ceremony Location',
			},
		},
		'/common/topic/description': 'Description',
	}),
	('/people/deceased_person', {
		'/people/deceased_person/date_of_death': 'Death Date',
		'/people/deceased_person/place_of_death': 'Death Place',
		'/people/deceased_person/cause_of_death': 'Death Cause',
	}),
	('/book/author', {
		'/book/author/works_written': 'Books',
		'/book/book_subject/works': 'Books About The Author',
		'/influence/influence_node/influenced': 'Influenced',
		'/influence/influence_node/influenced_by': 'Influenced By',
	}),
	('/film/actor', {
		'/film/actor/film': {
			'name': 'Films',
			'children': {
				'/film/performance/character': 'Character',
				'/film/performance/film': 'Film',
			},
		},
	}),
	('/tv/tv_actor', {
		'/tv/tv_actor/guest_roles': {
			'name': 'TV Series',
			'children': {
				'/tv/tv_guest_role/character': 'Character',
				'/tv/tv_guest_role/episodes_appeared_in': 'TV Series',
			}
		},
		'/tv/tv_actor/starring_roles': {
			'name': 'TV Series',
			'children': {
				'/tv/regular_tv_appearance/character': 'Character',
				'/tv/regular_tv_appearance/series': 'TV Series',
			},
		},
	}),
	('/organization/organization_founder', {
		'/organization/organization_founder/organizations_founded': 'Founded',
	}),
	('/business/board_member', {
		'/business/board_member/leader_of': {
			'name': 'Leadership',
			'children': {
				'/organization/leadership/from': 'From',
				'/organization/leadership/to': 'To',
				'/organization/leadership/organization': 'Organization',
				'/organization/leadership/role': 'Role',
				'/organization/leadership/title': 'Title',
			},
		},
		'/business/board_member/organization_board_memberships': {
			'name': 'Board Membership',
			'children': {
				'/organization/organization_board_membership/from': 'From',
				'/organization/organization_board_membership/to': 'To',
				'/organization/organization_board_membership/organization': 'Organization',
				'/organization/organization_board_membership/role': 'Role',
				'/organization/organization_board_membership/title': 'Title',
			},
		},
	}),
	('/sports/sports_league', {
		'/type/object/name': 'Name',
		'/sports/sports_league/championship': 'Championship',
		'/sports/sports_league/sport': 'Sport',
		'/organization/organization/slogan': 'Slogan',
		'/common/topic/official_website': 'Website',
		'/common/topic/description': 'Description',
		'/sports/sports_league/teams': {
			'name': 'Teams',
			'children': {
				'/sports/sports_league_participation/team': 'Team',
			},
		},
	}),
	('/sports/sports_team', {
		'/type/object/name': 'Name',
		'/common/topic/description': 'Description',
		'/sports/sports_team/sport': 'Sport',
		'/sports/sports_team/arena_stadium': 'Arena',
		'/sports/sports_team/championships': 'Championships',
		'/sports/sports_team/coaches': {
			'name': 'Coaches',
			'children': {
				'/sports/sports_team_coach_tenure/coach': 'Name',
				'/sports/sports_team_coach_tenure/position': 'Position',
				'/sports/sports_team_coach_tenure/from': 'From',
				'/sports/sports_team_coach_tenure/to': 'To',
			},
		},
		'/sports/sports_team/founded': 'Founded',
		'/sports/sports_team/league': {
			'name': 'League(s)',
			'children': {
				'/sports/sports_league_participation/league': 'League',
			},
		},
		'/sports/sports_team/location' : 'Location',
		'/sports/sports_team/roster': {
			'name': 'PlayerRoster',
			'children': {
				'/sports/sports_team_roster/player': 'Name',
				'/sports/sports_team_roster/position': 'Position',
				'/sports/sports_team_roster/number': 'Number',
				'/sports/sports_team_roster/from': 'From',
				'/sports/sports_team_roster/to': 'To',
			},
		},
	}),
	('/sports/professional_sports_team', {
		### empty
	}),
])