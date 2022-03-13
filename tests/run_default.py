from dash_entrypoints import run_entrypoint

# from dash_entrypoints.misc import get_local_ip_address
# from dash_entrypoints.multi_page.entrypoint import DEFAULT_VIEWS_MODULE

run_entrypoint(
    # app_name="TEST-APP",
    # ip_address=get_local_ip_address(),
    # views_module=DEFAULT_VIEWS_MODULE,
    # port=9050,
    debug=True,
)
