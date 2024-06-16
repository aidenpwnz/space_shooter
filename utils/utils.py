from os.path import join


def join_assets(asset_type: str, file: str) -> str:
    return join("assets", asset_type, file)
