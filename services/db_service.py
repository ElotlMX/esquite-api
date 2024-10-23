import typesense

client = typesense.Client(
    {
        "api_key": "xyz",
        "nodes": [{"host": "localhost", "port": "8108", "protocol": "http"}],
        "connection_timeout_seconds": 60,
    }
)

create_response = client.collections.create(
    {
        "name": "parallel_copora",
        "fields": [
            {"name": "id", "type": "auto"},
            # By default, locale = en that works fine with space sepparated langages
            # See: https://typesense.org/docs/27.1/api/collections.html#schema-parameters
            {"name": "l1", "type": "string", "stem": True, "locale": "en"},
            {"name": "l2", "type": "string"},
            {
                "name": "iso_variant",
                "type": "string",
                "facet": True,
                "sort": True,
            },
            {"name": "variant", "type": "string"},
            {"name": "name", "type": "string"},
            {"name": "pdf", "type": "string", "index": False},
            {
                "name": "authors",
                "type": "string[]",
                "facet": True,
                "optional": True,
            },
            {"name": "doc_id", "type": "string", "facet": True},
        ],
        "default_sorting_field": "iso_variant",
    }
)
