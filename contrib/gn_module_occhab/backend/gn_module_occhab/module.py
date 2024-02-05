from geonature.core.gn_commons.models import TModules
from .imports import (
    preprocess_transient_data,
    check_transient_data,
    import_data_to_occhab,
    remove_data_from_occhab,
)


class OcchabModule(TModules):
    __mapper_args__ = {"polymorphic_identity": "occhab"}

    _imports_ = {
        "preprocess_transient_data": preprocess_transient_data,
        "check_transient_data": check_transient_data,
        "import_data_to_destination": import_data_to_occhab,
        "remove_data_from_destination": remove_data_from_occhab,
        "statistics_labels": {
            "station_count": "Nombre de stations importées",
            "habitat_count": "Nombre d’habitats importés",
        },
    }
