"""{{ project_name }}."""

{% if versioning == "static" -%}
__version__ = "0.1.0"
{% elif build_backend == "hatchling" -%}
try:
    from importlib.metadata import version
    __version__ = version("{{ dist_name }}")
except ImportError:
    __version__ = "unknown"
{% else -%}
try:
    from ._version import __version__
except ImportError:
    __version__ = "unknown"
{% endif %}
