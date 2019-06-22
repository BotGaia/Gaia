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
* preference{"sport": "kitesurf", "locale": "Recife", "user_day": "sexta", "user_hour": "14"}
    - slot{"user_day": ["quarta", "sexta"]}
    - slot{"user_hour": "14"}
    - slot{"locale": ["lago paranoa", "Recife"]}
    - slot{"sport": "kitesurf"}
    - action_local
* choose
    - utter_time_before
* time_before{"hours_before": "2 horas"}
    - slot{"hours_before": "2 horas"}
    - action_user

## Generated Story 11
* preference{"sport": "kitesurf", "locale": "Recife", "user_day": "sexta", "user_hour": "14"}
    - slot{"user_day": ["quarta", "sexta"]}
    - slot{"user_hour": "14"}
    - slot{"locale": ["lago paranoa", "Recife"]}
    - slot{"sport": "kitesurf"}
    - action_local
* choose
    - utter_time_before
* time_before{"hours_before": "2 horas"}
    - slot{"hours_before": "2 horas"}
    - action_user

## Generated Story -3234865760225780992
* preference{"sport": "kitesurf", "locale": "Recife", "user_day": "sexta", "user_hour": "14"}
    - slot{"user_day": ["quarta", "sexta"]}
    - slot{"user_hour": "14"}
    - slot{"locale": ["lago paranoa", "Recife"]}
    - slot{"sport": "kitesurf"}
    - action_local
* choose
    - utter_time_before
* time_before{"minutes_before": "15 minutos"}
    - slot{"minutes_before": "15 minutos"}
    - action_user

## Generated Story -6422965880512245028
* greet
    - utter_greet
* preference{"sport": "surf", "user_day": "quarta", "user_hour": "10", "user_minute": "00", "locale": "lago parano\u00e1"}
    - slot{"user_day": ["quarta"]}
    - slot{"user_hour": "10"}
    - slot{"locale": ["lago parano\u00e1"]}
    - slot{"user_minute": "00"}
    - slot{"sport": "surf"}
    - action_local
* choose
    - utter_time_before
* time_before{"hours_before": "2 horas"}
    - slot{"hours_before": "2 horas"}
    - action_user
* preference{"sport": "kitesurf", "locale": "recife", "user_day": "sexta", "user_hour": "14"}
    - slot{"user_day": ["quarta", "sexta"]}
    - slot{"user_hour": "14"}
    - slot{"locale": ["lago paranoa", "recife"]}
    - slot{"sport": "kitesurf"}
    - action_local
* choose
    - utter_time_before
* time_before{"minutes_before": "30 minutos"}
    - slot{"minutes_before": "30 minutos"}
    - action_user
* preference{"sport": "vela", "locale": "brasilia", "user_day": "quarta", "user_hour": "19", "user_minute": "00"}
    - slot{"user_day": ["quarta"]}
    - slot{"user_hour": "19"}
    - slot{"locale": ["brasilia"]}
    - slot{"user_minute": "00"}
    - slot{"sport": "vela"}
    - action_local
* choose
    - utter_time_before

## Generated Story -95977543789797183
* greet
    - utter_greet
* preference{"sport": "surf", "user_day": "quarta", "user_hour": "10", "user_minute": "00", "locale": "guar\u00e1"}
    - slot{"user_day": ["quarta"]}
    - slot{"user_hour": "10"}
    - slot{"locale": ["guar\u00e1"]}
    - slot{"user_minute": "00"}
    - slot{"sport": "surf"}
    - action_local
* choose
    - utter_time_before
* time_before{"hours_before": "2 horas"}
    - slot{"hours_before": "2 horas"}
    - action_user
* preference{"sport": "stand up paddle", "user_day": "sabado", "user_hour": "9", "user_minute": "00", "locale": "lago paranoa"}
    - slot{"user_day": ["sabado"]}
    - slot{"user_hour": "9"}
    - slot{"locale": ["lago paranoa"]}
    - slot{"user_minute": "00"}
    - slot{"sport": "stand up paddle"}
    - action_local
* choose
    - utter_time_before
* time_before{"minutes_before": "30 minutos"}
    - slot{"minutes_before": "30 minutos"}
    - action_user
* greet
    - utter_greet
* preference{"sport": "vela", "user_day": "sexta", "user_hour": "11", "user_minute": "00", "locale": "rio de janeiro"}
    - slot{"locale": "rio de janeiro"}
    - slot{"user_day": ["sexta"]}
    - slot{"user_hour": "11"}
    - slot{"user_minute": "00"}
    - slot{"sport": "vela"}
    - action_local
* choose
    - utter_time_before
* time_before{"hours_before": "1 hora"}
    - slot{"hours_before": "1 hora"}
    - action_user

## Generated Story -1100676358352346366
* greet
    - utter_greet
* preference{"sport": "kitesurf", "user_day": "quinta", "user_hour": "11", "user_minute": "00", "locale": "rio de janeiro"}
    - slot{"user_day": ["quinta"]}
    - slot{"user_hour": "11"}
    - slot{"locale": ["rio de janeiro"]}
    - slot{"user_minute": "00"}
    - slot{"sport": "kitesurf"}
    - action_local
* choose
    - utter_time_before
* time_before{"hours_before": "3 horas"}
    - slot{"hours_before": "3 horas"}
    - action_user
* preference{"sport": "vela", "user_day": "sexta", "user_hour": "19", "user_minute": "00", "locale": "guaruj\u00e1"}
    - slot{"user_day": ["sexta"]}
    - slot{"user_hour": "19"}
    - slot{"locale": ["guaruj\u00e1"]}
    - slot{"user_minute": "00"}
    - slot{"sport": "vela"}
    - action_local
* choose
    - utter_time_before
* time_before{"hours_before": "7 horas"}
    - slot{"hours_before": "7 horas"}
    - action_user
* preference{"sport": "surf", "user_day": "quinta", "user_hour": "14", "user_minute": "00", "locale": "ilhabela"}
    - slot{"user_day": ["ter\u00e7a", "quinta"]}
    - slot{"user_hour": "14"}
    - slot{"locale": ["ilhabela"]}
    - slot{"user_minute": "00"}
    - slot{"sport": "surf"}
    - action_local
* choose
    - utter_time_before
* time_before{"minutes_before": "30 minutos"}
    - slot{"minutes_before": "30 minutos"}
    - action_user
* preference{"sport": "stand up paddle", "user_day": "quinta", "user_hour": "10", "user_minute": "00", "locale": "lago paranoa"}
    - slot{"user_day": ["ter\u00e7a", "quinta"]}
    - slot{"user_hour": "10"}
    - slot{"locale": ["lago paranoa"]}
    - slot{"user_minute": "00"}
    - slot{"sport": "stand up paddle"}
    - action_local
*choose
    - utter_time_before
* time_before{"minutes_before": "40 minutos"}
    - slot{"minutes_before": "40 minutos"}
    - action_user

## Generated Story 2076172119833102731
* greet
    - utter_greet
* preference{"sport": "surf", "user_day": "quarta", "user_hour": "10", "user_minute": "00", "locale": "rio de janeiro"}
    - slot{"user_day": ["quarta"]}
    - slot{"user_hour": "10"}
    - slot{"locale": ["rio de janeiro"]}
    - slot{"user_minute": "00"}
    - slot{"sport": "surf"}
    - action_local
*choose
    - utter_time_before
* time_before{"hours_before": "2 horas"}
    - slot{"hours_before": "2 horas"}
    - action_user
* preference{"sport": "vela", "user_day": "quinta", "user_hour": "13", "user_minute": "00", "locale": "guaruja"}
    - slot{"user_day": ["quinta"]}
    - slot{"user_hour": "13"}
    - slot{"locale": ["guaruja"]}
    - slot{"user_minute": "00"}
    - slot{"sport": "vela"}
    - action_local
* choose
    - utter_time_before
* time_before{"minutes_before": "30 minutos"}
    - slot{"minutes_before": "30 minutos"}
    - action_user
* preference{"sport": "stand up paddle", "user_day": "sexta", "user_hour": "12", "user_minute": "00", "locale": "lago paranoa"}
    - slot{"user_day": ["sexta"]}
    - slot{"user_hour": "12"}
    - slot{"locale": ["lago paranoa"]}
    - slot{"user_minute": "00"}
    - slot{"sport": "stand up paddle"}
    - action_local
* choose
    - utter_time_before
* time_before{"hours_before": "3 horas"}
    - slot{"hours_before": "3 horas"}
    - action_user

## Generated Story -514383783422040419
* greet
    - utter_greet
* preference{"sport": "surf", "user_day": "quarta", "user_hour": "10", "locale": "guaruj\u00e1"}
    - slot{"user_day": ["quarta"]}
    - slot{"user_hour": "10"}
    - slot{"locale": ["guaruj\u00e1"]}
    - slot{"sport": "surf"}
    - action_local
*choose
    - utter_time_before
* time_before{"minutes_before": "30 minutos"}
    - slot{"minutes_before": "30 minutos"}
    - action_user
* preference{"sport": "kitesurf", "user_day": "quinta", "user_hour": "13", "user_minute": "00", "locale": "bahia"}
    - slot{"user_day": ["quinta"]}
    - slot{"user_hour": "13"}
    - slot{"locale": ["bahia"]}
    - slot{"user_minute": "00"}
    - slot{"sport": "kitesurf"}
    - action_local
* choose
    - utter_time_before
* time_before{"hours_before": "4 horas"}
    - slot{"hours_before": "4 horas"}
    - action_user

## Generated Story -1656233441744573291
* greet
    - utter_greet
* preference{"sport": "surf", "user_day": "quarta", "user_hour": "10", "user_minute": "0 minutos", "locale": "brasilia"}
    - slot{"user_day": ["quarta"]}
    - slot{"user_hour": "10"}
    - slot{"locale": ["brasilia"]}
    - slot{"user_minute": "0 minutos"}
    - slot{"sport": "surf"}
    - action_local
* choose
    - utter_time_before
* time_before{"hours_before": "3 horas"}
    - slot{"hours_before": "3 horas"}
    - action_user
* preference{"sport": "kitesurf", "user_day": "quinta", "user_hour": "17", "locale": "bahia"}
    - slot{"user_day": ["ter\u00e7a", "quarta", "quinta"]}
    - slot{"user_hour": "17"}
    - slot{"locale": ["bahia"]}
    - slot{"sport": "kitesurf"}
    - action_local
* choose
    - utter_time_before
* time_before{"minutes_before": "30 minutos"}
    - slot{"minutes_before": "30 minutos"}
    - action_user
* preference{"sport": "vela", "user_day": "sabado", "user_hour": "15", "user_minute": "30 minutos", "locale": "lago paranoa"}
    - slot{"user_day": ["sabado"]}
    - slot{"user_hour": "15"}
    - slot{"locale": ["lago paranoa"]}
    - slot{"user_minute": "30 minutos"}
    - slot{"sport": "vela"}
    - action_local
* choose
    - utter_time_before
* time_before{"minutes_before": "40 minutos"}
    - slot{"minutes_before": "40 minutos"}
    - action_user

## Generated Story 6375185026803936177
* greet
    - utter_greet
* elaborate_sport
    - utter_elaborate_local
* locale{"locale": "goiania"}
    - slot{"locale": "goiania"}
    - action_local
    - slot{"type": null}
* choose{"choice": "1"}
    - slot{"choice": "1"}
    - action_sports
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
* locale{"locale": "gama"}
    - slot{"locale": "gama"}
    - action_local
    - slot{"type": null}
* choose{"choice": "3"}
    - slot{"choice": "3"}
    - action_sunrise_sunset
* elaborate_pressure{"type": "press\u00e3o"}
    - slot{"type": "press\u00e3o"}
    - utter_elaborate_local
* locale{"locale": "bahia"}
    - slot{"locale": "bahia"}
    - action_local
    - slot{"type": null}
* choose{"choice": "1"}
    - slot{"choice": "1"}
    - action_pressure
* elaborate_wind
    - utter_elaborate_local
* locale{"locale": "brasilia"}
    - slot{"locale": "brasilia"}
    - action_local
    - slot{"type": null}
* choose{"choice": "2"}
    - slot{"choice": "2"}
    - action_wind

