"""
Geonames Search API: http://www.geonames.org/export/geonames-search.html
"""

import geonames.adapters.base


class Search(geonames.adapters.base.AdapterBase):
    service_name = 'search'

    def get_required_parameters(self):
        return []

    def query(self, value):
        return self.set_string_parameter('q', value)

    def place_name_like(self, value):
        return self.set_string_parameter('name', value)

    def place_name_equals(self, value):
        return self.set_string_parameter('name_equals', value)

    def place_name_starts_with(self, value):
        return self.set_string_parameter('name_startsWith', value)

    def max_rows(self, value):
        return self.set_string_parameter('maxRows', value)

    def start_row(self, value):
        return self.set_string_parameter('startRow', value)

    def country(self, value):
        """Expects an ISO-3166 two-letter country-code."""

        return self.set_string_parameter('country', value)

    def show_country_first(self, value):
        """Show this country first."""

        return self.set_string_parameter('countryBias', value)

    def continent(self, value):
        """Expects a two-letter continent code."""

        return self.set_string_parameter('continentCode', value)

    def admin_code1(self, value):
        return self.set_string_parameter('adminCode1', value)

    def admin_code2(self, value):
        return self.set_string_parameter('adminCode2', value)

    def admin_code3(self, value):
        return self.set_string_parameter('adminCode3', value)

    def feature_class(self, value):
        """See http://www.geonames.org/export/codes.html ."""

        return self.set_string_parameter('featureClass', value)

    def feature_code(self, value):
        """See http://www.geonames.org/export/codes.html ."""

        return self.set_string_parameter('featureCode', value)

    def population_class(self, value):
        """See http://download.geonames.org/export/dump/readme.txt ."""

# TODO(dustin): It's unclear whether multiple values are allowed and how they'd 
#               be delimited.

        return self.set_string_parameter('cities', value)

    def language(self, value):
        """ISO-366 two-letter language code."""

        return self.set_string_parameter('lang', value)

    def verbosity(self, value):
        value = value.upper()
        return self.set_string_parameter('style', value)

    def force_matching_name(self):
        """We'll only get results where the search-term is definitely in the name."""

        return self.set_boolean_parameter('isNameRequired', True)

    def tag(self, value):
        return self.set_string_parameter('tag', value)

    def operator(self, value):
        """The logical conjunction between all of the search terms."""

        return self.set_string_parameter('operator', value)

    def charset(self, value):
        return self.set_string_parameter('charset', value)        

    def fuzzy(self, value):
        return self.set_string_parameter('fuzzy', value)

    def east_west_north_south_box(self, value):
        return self.set_string_parameter('east,west,north,south', value)

    def place_name_language(self, value):
        return self.set_string_parameter('searchlang', value)

    def order_by(self, value):
        return self.set_string_parameter('orderby', value)
