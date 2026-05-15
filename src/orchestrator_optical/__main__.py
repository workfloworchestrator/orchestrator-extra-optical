import argparse
import os


def scaffold(output_dir: str):
    """Generates the static boilerplate for an organization to extend."""
    port_file_content = """
from orchestrator.domain.base import ProductBlockModel
from orchestrator_optical.mixins.ports import TrxClientFieldsInactive, TrxClientFieldsActive

class CustomTrxClientInactive(ProductBlockModel, TrxClientFieldsInactive, product_block_name="CustomTrxClient"):
    # TODO: Add your custom IRM/CRM fields here
    pass

class CustomTrxClientActive(CustomTrxClientInactive, TrxClientFieldsActive):
    pass
"""
    os.makedirs(output_dir, exist_ok=True)
    with open(f"{output_dir}/custom_optical_ports.py", "w") as f:
        f.write(port_file_content.strip())

    print(f"✅ Successfully scaffolded optical models in {output_dir}/")
    print("You can now safely add your business logic without modifying the core module.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=["scaffold"])
    parser.add_argument("--dir", default="products/optical_blocks")
    args = parser.parse_args()

    if args.command == "scaffold":
        scaffold(args.dir)
