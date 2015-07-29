import logging

import geonames.config.api
import geonames.compat

logging.getLogger('requests.packages.urllib3.connectionpool').setLevel(logging.WARNING)

import requests
import lxml.etree

_LOGGER = logging.getLogger(__name__)


class Result(object):
    def __init__(self, xml_object):
        self.__xml = xml_object

    def get_xml_nodes(self):
        """Return a list of raw XML nodes."""

        return self.xml.xpath(
                ".//gn:Feature", 
                namespaces=geonames.config.api.XML_NAMESPACES)

    def get_flat_results(self):
        """Just yield a list of 2-tuples of ID and name."""

        for node in self.get_xml_nodes():
            feature_node = \
                node.xpath(
                    './/@rdf:about', 
                    namespaces=geonames.config.api.XML_NAMESPACES)

            feature_id = str(feature_node[0])

            name_node = \
                node.xpath(
                    './/gn:name', 
                    namespaces=geonames.config.api.XML_NAMESPACES)

            name = geonames.compat.make_unicode(name_node[0].text)

            yield (feature_id, name)

    @property
    def xml(self):
        return self.__xml


class AdapterBase(object):
    # This needs to be populated by child.
    service_name = None

    def __init__(self, username):
        service_name = self.__class__.service_name

        assert \
            service_name is not None, \
            "service_name needs to be set."

        self.__url = geonames.config.api.API_URL_PREFIX + '/' + service_name
        self.__parameters_list = [
            ('type', 'rdf'),
            ('username', username),
        ]

    def get_required_parameters(self):
        raise NotImplementedError()

    def validate_parameters(self, parameters_list):
        pass

    def distill_parameters(self, parameters_list):
        pass

    def set_string_parameter(self, key, value):
        self.__parameters_list.append((key, value))

        return self

    def set_boolean_parameter(self, key, value):
# TODO(dustin): How do we represent these?
        self.__parameters_list.append((key, bool(value)))

        return self

    def __flatten_parameters(self):
        return geonames.compat.urlencode(self.__parameters_list)

    def execute(self):
        """Return an lxml object."""

        _LOGGER.debug("Submitting parameters:\n%s", self.__parameters_list)

        self.distill_parameters(self.__parameters_list)
        required = self.get_required_parameters()
        required_s = set(required)
        have_s = set([k for (k, v) in self.__parameters_list])

        if required_s.issubset(have_s) is False:
            raise ValueError("We're missing one or more required parameters: "
                             "{0}".format(required))

        self.validate_parameters(self.__parameters_list)

        parameters = self.__flatten_parameters()

        headers = {
            'Accept': 'text/xml',
        }

        r = requests.get(
                self.__url, 
                params=parameters, 
                headers=headers, 
                stream=True)

        r.raise_for_status()

        return Result(lxml.etree.fromstring(r.raw.read()))
