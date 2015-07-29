------------
Introduction
------------

This is a client library for the `Geonames <http://www.geonames.org>`_ RDF-compatible `web-services <http://www.geonames.org/export/ws-overview.html>`_. At this time, only the `Search API <http://www.geonames.org/export/geonames-search.html>`_ provides RDF responses and is, therefore, the only adapter available.

RDF is often used in association with the `Semantic Web <http://www.w3.org/standards/semanticweb>`_ and/or the `IoT <https://en.wikipedia.org/wiki/Internet_of_Things>`_.


------------
Requirements
------------

- requests
- Python 2.x or 3.x


------------
Installation
------------

Via PyPI::

    $ sudo pip install geonames_rdf


-----
Usage
-----

As a library::

    import geonames.adapters.search

    _USERNAME = 'your_username'
    sa = geonames.adapters.search.Search(_USERNAME)

    result = sa.query('detroit').country('us').max_rows(5).execute()
    for id_, name in result.get_flat_results():
        # make_unicode() is only used here for Python version-compatibility.
        print(geonames.compat.make_unicode("[{0}]: [{1}]").format(id_, name))

A result object will be returned from the `execute()` method. The following are the ways to read the results (`get_flat_results` is used above):

- The raw *lxml* object is exposed through the `xml` property.
- The `get_xml_nodes` method will return a list of `Feature` `lxml.etree` objects from the resulting document, representing each of the results.
- The `get_flat_results` method will simply yields a list of (id, name) 2-tuples if you're not interested in anything else. This is also what's returned, by default, from the command-line utility.

As a command-line utility::

    $ gn_search dsoprea -p query detroit -p country us -p max_rows 5
    [http://sws.geonames.org/4990729/]: [Detroit]
    [http://sws.geonames.org/6955112/]: [Detroit-Warren-Livonia]
    [http://sws.geonames.org/5024238/]: [Detroit Lakes Airport]
    [http://sws.geonames.org/4990733/]: [Detroit City Airport]
    [http://sws.geonames.org/4990742/]: [Detroit Metropolitan Wayne County Airport]

You may only provide string (non-boolean) parameters to the command-line utility.

**NOTE:** You can also get the complete RDF response by passing the "-x" parameter.

Whether you're using the library or the tool, the parameters that are available are:

=========================  =====================
Library Parameter Name     API Parameter Name
=========================  =====================
query                      q
place_name_like            name
place_name_equals          name_equals
place_name_starts_with     name_startsWith
max_rows                   maxRows
start_row                  startRow
country                    country
show_country_first         countryBias
continent                  continentCode
admin_code1                adminCode1
admin_code2                adminCode2
admin_code3                adminCode3
feature_class              featureClass
feature_code               featureCode
population_class           cities
language                   lang
verbosity                  style
force_matching_name        isNameRequired
tag                        tag
operator                   operator
charset                    charset
fuzzy                      fuzzy
east_west_north_south_box  east,west,north,south
place_name_language        searchlang
order_by                   orderby
=========================  =====================

Some of the parameters can be specified more than once. See the API documentation for more information.

------------
Design Notes
------------

- Note that most of the parameters in the library are named differently from the API. Normally this goes against my policy, but I found so many of the parameters to be ambiguous or cryptic that I renamed those parameters to be clearer and just renamed the rest to underscore-separated naming while I was at it.

- We mostly rely on the API to correctly validate against bad parameters. We don't like arbitrarily validating parameters in the client since the rules may change in the server and it's one more thing that might interfere with your implementation. However, if there is a type of validation that, for one reason or another, makes sense and/or would make things easier to develop against, let me know.
