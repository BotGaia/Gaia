## Generated Story 1
* greet
    - utter_greet
* locale{"locale": "brasilia"}
    - slot{"locale": "brasilia"}
    - action_weather
* temperature{"locale": "manaus"}
    - slot{"locale": "manaus"}
    - action_temperature
* wind{"locale": "aguas claras"}
    - slot{"locale": "aguas claras"}
    - action_wind
* sunrise_sunset{"locale": "salinas"}
    - slot{"locale": "salinas"}
    - action_sunrise_sunset
* humidity{"locale": "paris"}
    - slot{"locale": "paris"}
    - action_humidity
* goodbye
    - utter_goodbye

## Generated Story 2
* greet
    - utter_greet
* temperature{"type": "temperatura", "locale": "brasilia"}
    - slot{"locale": "brasilia"}
    - slot{"type": "temperatura"}
    - action_local
    - slot{"type": null}
* choose{"choice": "2"}
    - slot{"choice": "2"}
    - action_temperature
* inform{"locale": "goiania"}
    - slot{"locale": "goiania"}
    - action_local
    - slot{"type": null}
* choose{"choice": "1"}
    - slot{"choice": "1"}
    - action_weather

## Generated Story 3
* greet
    - utter_greet
* sports{"locale": "brasilia"}
    - slot{"locale": "brasilia"}
    - action_sports

## Generated Story 4
* greet
    - utter_greet
* sports{"locale": "brasilia"}
    - slot{"locale": "brasilia"}
    - action_local
    - slot{"type": null}
* choose{"choice": "2"}
    - slot{"choice": "2"}
    - action_sports
* sports{"locale": "Nova Iorque Brasil"}
    - slot{"locale": "Nova Iorque Brasil"}
    - action_local
    - slot{"type": null}
* greet
    - utter_greet
* sports{"locale": "brasilia"}
    - slot{"locale": "brasilia"}
    - action_local
    - slot{"type": null}
* choose{"choice": "4"}
    - slot{"choice": "4"}
    - action_sports
* goodbye
    - utter_goodbye

## Generated Story 5
* greet
    - utter_greet
* specific_sport{"sport": "kitesurf", "locale": "brasilia"}
    - slot{"locale": "brasilia"}
    - slot{"sport": "kitesurf"}
    - action_local
    - slot{"type": null}
* choose{"choice": "2"}
    - slot{"choice": "2"}
    - action_specific_sport
* specific_sport{"sport": "surf", "locale": "brasilia"}
    - slot{"locale": "brasilia"}
    - slot{"sport": "surf"}
    - action_local
    - slot{"type": null}
* choose{"choice": "2"}
    - slot{"choice": "2"}
    - action_specific_sport

## Generated Story 6
* greet
    - utter_greet
* sports{"locale": "brasilia"}
    - slot{"locale": "brasilia"}
    - action_local
    - slot{"type": null}
* choose{"choice": "2"}
    - slot{"choice": "2"}
    - action_sports
* inform{"locale": "brasilia"}
    - slot{"locale": "brasilia"}
    - action_local
    - slot{"type": null}
* choose{"choice": "3"}
    - slot{"choice": "3"}
    - action_weather

## Generated Story 7
* greet
    - utter_greet
* inform{"locale": "gama"}
    - slot{"locale": "gama"}
    - action_local
    - slot{"type": null}
* choose{"choice": "3"}
    - slot{"choice": "3"}
    - action_weather
* sports{"locale": "brasilia"}
    - slot{"locale": "brasilia"}
    - action_local
    - slot{"type": null}
* choose{"choice": "2"}
    - slot{"choice": "2"}
    - action_sports

## Generated Story 8
* greet
    - utter_greet
* locale{"locale": "brasilia"}
    - slot{"locale": "brasilia"}
    - action_local
    - slot{"type": null}
* choose{"choice": "2"}
    - slot{"choice": "2"}
    - action_weather

## Generated Story 9
* greet
    - utter_greet
* locale{"locale": "brasilia"}
    - slot{"locale": "brasilia"}
    - action_local
    - slot{"type": null}
* choose{"choice": "2"}
    - slot{"choice": "2"}
    - action_weather
* locale{"locale": "gama"}
    - slot{"locale": "gama"}
    - action_local
    - slot{"type": null}
* choose{"choice": "3"}
    - slot{"choice": "3"}
    - action_weather
* locale{"locale": "manaus"}
    - slot{"locale": "manaus"}
    - action_local
    - slot{"type": null}
* choose{"choice": "1"}
    - slot{"choice": "1"}
    - action_weather
* greet
    - utter_greet
* locale{"locale": "goias"}
    - slot{"locale": "goias"}
    - action_local
    - slot{"type": null}
* choose{"choice": "1"}
    - slot{"choice": "1"}
    - action_weather

## Generated Story 10
* preference{"user_sport": "kitesurf", "user_locale": "Recife", "user_day": "sexta", "user_hour": "14"}
    - slot{"user_day": ["quarta", "sexta"]}
    - slot{"user_hour": "14"}
    - slot{"user_locale": ["lago paranoa", "Recife"]}
    - slot{"user_sport": "kitesurf"}
    - utter_time_before
* time_before{"hours_before": "2 horas"}
    - slot{"hours_before": "2 horas"}
    - action_user

## Generated Story 11
* preference{"user_sport": "kitesurf", "user_locale": "Recife", "user_day": "sexta", "user_hour": "14"}
    - slot{"user_day": ["quarta", "sexta"]}
    - slot{"user_hour": "14"}
    - slot{"user_locale": ["lago paranoa", "Recife"]}
    - slot{"user_sport": "kitesurf"}
    - utter_time_before
* time_before{"hours_before": "2 horas"}
    - slot{"hours_before": "2 horas"}
    - action_user

## Generated Story -3234865760225780992
* preference{"user_sport": "kitesurf", "user_locale": "Recife", "user_day": "sexta", "user_hour": "14"}
    - slot{"user_day": ["quarta", "sexta"]}
    - slot{"user_hour": "14"}
    - slot{"user_locale": ["lago paranoa", "Recife"]}
    - slot{"user_sport": "kitesurf"}
    - utter_time_before
* time_before{"minutes_before": "15 minutos"}
    - slot{"minutes_before": "15 minutos"}
    - action_user

## Generated Story -6422965880512245028
* greet
    - utter_greet
* preference{"user_sport": "surf", "user_day": "quarta", "user_hour": "10", "user_minute": "00", "user_locale": "lago parano\u00e1"}
    - slot{"user_day": ["quarta"]}
    - slot{"user_hour": "10"}
    - slot{"user_locale": ["lago parano\u00e1"]}
    - slot{"user_minute": "00"}
    - slot{"user_sport": "surf"}
    - utter_time_before
* time_before{"hours_before": "2 horas"}
    - slot{"hours_before": "2 horas"}
    - action_user
* preference{"user_sport": "kitesurf", "user_locale": "recife", "user_day": "sexta", "user_hour": "14"}
    - slot{"user_day": ["quarta", "sexta"]}
    - slot{"user_hour": "14"}
    - slot{"user_locale": ["lago paranoa", "recife"]}
    - slot{"user_sport": "kitesurf"}
    - utter_time_before
* time_before{"minutes_before": "30 minutos"}
    - slot{"minutes_before": "30 minutos"}
    - action_user
* preference{"user_sport": "vela", "user_locale": "brasilia", "user_day": "quarta", "user_hour": "19", "user_minute": "00"}
    - slot{"user_day": ["quarta"]}
    - slot{"user_hour": "19"}
    - slot{"user_locale": ["brasilia"]}
    - slot{"user_minute": "00"}
    - slot{"user_sport": "vela"}
    - utter_time_before

## Generated Story -95977543789797183
* greet
    - utter_greet
* preference{"user_sport": "surf", "user_day": "quarta", "user_hour": "10", "user_minute": "00", "user_locale": "guar\u00e1"}
    - slot{"user_day": ["quarta"]}
    - slot{"user_hour": "10"}
    - slot{"user_locale": ["guar\u00e1"]}
    - slot{"user_minute": "00"}
    - slot{"user_sport": "surf"}
    - utter_time_before
* time_before{"hours_before": "2 horas"}
    - slot{"hours_before": "2 horas"}
    - action_user
* preference{"user_sport": "stand up paddle", "user_day": "sabado", "user_hour": "9", "user_minute": "00", "user_locale": "lago paranoa"}
    - slot{"user_day": ["sabado"]}
    - slot{"user_hour": "9"}
    - slot{"user_locale": ["lago paranoa"]}
    - slot{"user_minute": "00"}
    - slot{"user_sport": "stand up paddle"}
    - utter_time_before
* time_before{"minutes_before": "30 minutos"}
    - slot{"minutes_before": "30 minutos"}
    - action_user
* greet
    - utter_greet
* preference{"user_sport": "vela", "user_day": "sexta", "user_hour": "11", "user_minute": "00", "locale": "rio de janeiro"}
    - slot{"locale": "rio de janeiro"}
    - slot{"user_day": ["sexta"]}
    - slot{"user_hour": "11"}
    - slot{"user_minute": "00"}
    - slot{"user_sport": "vela"}
    - utter_time_before
* time_before{"hours_before": "1 hora"}
    - slot{"hours_before": "1 hora"}
    - action_user

## Generated Story -1100676358352346366
* greet
    - utter_greet
* preference{"user_sport": "kitesurf", "user_day": "quinta", "user_hour": "11", "user_minute": "00", "user_locale": "rio de janeiro"}
    - slot{"user_day": ["quinta"]}
    - slot{"user_hour": "11"}
    - slot{"user_locale": ["rio de janeiro"]}
    - slot{"user_minute": "00"}
    - slot{"user_sport": "kitesurf"}
    - utter_time_before
* time_before{"hours_before": "3 horas"}
    - slot{"hours_before": "3 horas"}
    - action_user
* preference{"user_sport": "vela", "user_day": "sexta", "user_hour": "19", "user_minute": "00", "user_locale": "guaruj\u00e1"}
    - slot{"user_day": ["sexta"]}
    - slot{"user_hour": "19"}
    - slot{"user_locale": ["guaruj\u00e1"]}
    - slot{"user_minute": "00"}
    - slot{"user_sport": "vela"}
    - utter_time_before
* time_before{"hours_before": "7 horas"}
    - slot{"hours_before": "7 horas"}
    - action_user
* preference{"user_sport": "surf", "user_day": "quinta", "user_hour": "14", "user_minute": "00", "user_locale": "ilhabela"}
    - slot{"user_day": ["ter\u00e7a", "quinta"]}
    - slot{"user_hour": "14"}
    - slot{"user_locale": ["ilhabela"]}
    - slot{"user_minute": "00"}
    - slot{"user_sport": "surf"}
    - utter_time_before
* time_before{"minutes_before": "30 minutos"}
    - slot{"minutes_before": "30 minutos"}
    - action_user
* preference{"user_sport": "stand up paddle", "user_day": "quinta", "user_hour": "10", "user_minute": "00", "user_locale": "lago paranoa"}
    - slot{"user_day": ["ter\u00e7a", "quinta"]}
    - slot{"user_hour": "10"}
    - slot{"user_locale": ["lago paranoa"]}
    - slot{"user_minute": "00"}
    - slot{"user_sport": "stand up paddle"}
    - utter_time_before
* time_before{"minutes_before": "40 minutos"}
    - slot{"minutes_before": "40 minutos"}
    - action_user

