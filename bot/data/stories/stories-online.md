## Generated Story 1
* humidity{"type": "umidade", "locale": "brasilia"}
    - slot{"locale": "brasilia"}
    - slot{"type": "umidade"}
    - action_local
    - slot{"type": null}
* choose{"choice": "4"}
    - slot{"choice": "4"}
    - action_humidity
* greet
    - utter_greet
* sky{"type": "ceu", "locale": "recife"}
    - slot{"locale": "recife"}
    - slot{"type": "ceu"}
    - action_local
    - slot{"type": null}
* choose{"choice": "1"}
    - slot{"choice": "1"}
    - action_sky

## Generated Story 2
* greet
    - utter_greet
* sports{"locale": "brasilia"}
    - slot{"locale": "brasilia"}
    - action_local
    - slot{"type": null}
* choose{"choice": "2"}
    - slot{"choice": "2"}
    - action_sports
* goodbye
    - utter_goodbye
* greet
    - utter_greet
* sports{"locale": "Nova Iorque Brasil"}
    - slot{"locale": "Nova Iorque Brasil"}
    - action_local

## Generated Story 3778712413651407244
* greet
    - utter_greet
* elaborate_temperature
    - utter_elaborate_local
* locale{"locale": "brasilia"}
    - slot{"locale": "brasilia"}
    - action_local
    - slot{"type": null}
* choose{"choice": "2"}
    - slot{"choice": "2"}
    - action_temperature
* elaborate_sun
    - utter_elaborate_local
* locale{"locale": "goiania"}
    - slot{"locale": "goiania"}
    - action_local
    - slot{"type": null}
* choose{"choice": "1"}
    - slot{"choice": "1"}
    - action_sunrise_sunset
* elaborate_sport
    - utter_elaborate_local
* locale{"locale": "maceio"}
    - slot{"locale": "maceio"}
    - action_local
    - slot{"type": null}
* choose{"choice": "1"}
    - slot{"choice": "1"}
    - action_sports
* elaborate_sport{"type": "esporte"}
    - slot{"type": "esporte"}
    - utter_elaborate_local
* locale{"locale": "guaruja"}
    - slot{"locale": "guaruja"}
    - action_local
    - slot{"type": null}
* choose{"choice": "1"}
    - slot{"choice": "1"}
    - action_sports
* elaborate_wind
    - utter_elaborate_local
* locale{"locale": "taguatinga"}
    - slot{"locale": "taguatinga"}
    - action_local

## Generated Story 3721559633672000720
* greet
    - utter_greet
* help
    - utter_help
* example_sport
    - utter_example_sport
* specific_sport{"sport": "surf", "locale": "sao paulo"}
    - slot{"locale": "sao paulo"}
    - slot{"sport": "surf"}
    - action_local
* choose{"choice": "1"}
    - slot{"choice": "1"}
    - action_specific_sport
* specific_sport
    - utter_example_sport
* specific_sport{"sport": "kitesurf", "locale": "rio de janeiro"}
    - slot{"locale": "rio de janeiro"}
    - slot{"sport": "kitesurf"}
    - action_local
    - slot{"type": null}
* choose{"choice": "1"}
    - slot{"choice": "1"}
    - action_specific_sport
* example_sport
    - utter_example_sport
* sports{"locale": "lago paranoa"}
    - slot{"locale": "lago paranoa"}
    - action_local
    - slot{"type": null}
* choose{"choice": "1"}
    - slot{"choice": "1"}
    - action_sports
* help
    - utter_help
* notification
    - utter_create_notification
* preference{"sport": "kitesurf", "user_day": "quinta", "user_hour": "8", "user_minute": "20 minutos", "locale": "lago paranoa"}
    - slot{"locale": "lago paranoa"}
    - slot{"sport": "kitesurf"}
    - slot{"user_day": ["quinta"]}
    - slot{"user_hour": "8"}
    - slot{"user_minute": "20 minutos"}
    - action_local
    - slot{"type": null}
* choose{"choice": "1"}
    - slot{"choice": "1"}
    - utter_time_before
* time_before{"minutes_before": "10 minutos"}
    - slot{"minutes_before": "10 minutos"}
    - action_user

## Generated Story 1312342511481818637
* greet
    - utter_greet
* elaborate_temperature
    - utter_elaborate_local
* locale{"locale": "brasilia"}
    - slot{"locale": "brasilia"}
    - action_local
    - slot{"type": null}
* choose{"choice": "2"}
    - slot{"choice": "2"}
    - action_temperature
* elaborate_sun
    - utter_elaborate_local
* locale{"locale": "goiania"}
    - slot{"locale": "goiania"}
    - action_local
    - slot{"type": null}
* choose{"choice": "1"}
    - slot{"choice": "1"}
    - action_sunrise_sunset
* elaborate_sun
    - utter_elaborate_local
* locale{"locale": "manaus"}
    - slot{"locale": "manaus"}
    - action_local
    - slot{"type": null}
* choose{"choice": "1"}
    - slot{"choice": "1"}
    - action_sunrise_sunset
* elaborate_sport
    - utter_elaborate_local
* locale{"locale": "bahia"}
    - slot{"locale": "bahia"}
    - action_local
    - slot{"type": null}
* choose{"choice": "1"}
    - slot{"choice": "1"}
    - action_sports
* sports{"locale": "taguatinga"}
    - slot{"locale": "taguatinga"}
    - action_local
    - slot{"type": null}
* choose{"choice": "2"}
    - slot{"choice": "2"}
    - action_sports
* elaborate_sport
    - utter_elaborate_local
* locale{"locale": "gama"}
    - slot{"locale": "gama"}
    - action_local
    - slot{"type": null}
* choose{"choice": "1"}
    - slot{"choice": "1"}
    - action_sports
* inform{"locale": "taguatinga"}
    - slot{"locale": "taguatinga"}
    - action_local
    - slot{"type": null}
* choose{"choice": "2"}
    - slot{"choice": "2"}
    - action_weather
* sports{"locale": "Bras\u00edlia"}
    - slot{"locale": "Bras\u00edlia"}
    - action_local
    - slot{"type": null}
* choose{"choice": "2"}
    - slot{"choice": "2"}
    - action_sports
* sports{"locale": "Bras\u00edlia"}
    - slot{"locale": "Bras\u00edlia"}
    - action_local
    - slot{"type": null}
* choose{"choice": "2"}
    - slot{"choice": "2"}
    - action_sports
* all_cyclones
    - action_all_cyclones
    - utter_after_all_cyclones
* all_cyclones
    - action_all_cyclones
    - utter_after_all_cyclones

