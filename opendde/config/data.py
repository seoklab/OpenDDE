# pylint: disable=C0114
import os
from pathlib import Path
from typing import Any


def default_root_dir() -> str:
    """Fallback OpenDDE root used when ``OPENDDE_ROOT_DIR`` is unset."""
    return "/home.galaxy4/share/OpenDDE"


OPENDDE_ROOT_DIR = os.environ.get("OPENDDE_ROOT_DIR", default_root_dir())
DATA_ROOT = OPENDDE_ROOT_DIR
SEARCH_DATABASE_ROOT = os.path.join(OPENDDE_ROOT_DIR, "search_database")

data_configs: dict[str, Any] = {
    "msa": {
        "enable_prot_msa": True,
        # Upper bound for data-side MSA feature assembly before model sampling.
        "msa_pool_size": 16384,
        # Fixed number of MSA rows consumed by the MSA stack during prediction.
        "msa_depth": 1280,
        "max_paired_per_species": 600,
        # Per-input-A3M read cap. <= 0 means read all sequences from each MSA file.
        "max_input_sequences": -1,
    },
    "template": {
        "enable_prot_template": True,
        "max_templates": 4,
        "fetch_remote": True,
        "prot_template_mmcif_dir": os.path.join(SEARCH_DATABASE_ROOT, "mmcif"),
        "prot_template_cache_dir": "",
        "kalign_binary_path": "kalign",
        "release_dates_path": os.path.join(DATA_ROOT, "common/release_date_cache.json"),
        "obsolete_pdbs_path": os.path.join(
            DATA_ROOT, "common/obsolete_to_successor.json"
        ),
    },
    "ccd_components_file": os.path.join(DATA_ROOT, "common/components.cif"),
    "ccd_components_rdkit_mol_file": os.path.join(
        DATA_ROOT, "common/components.cif.rdkit_mol.pkl"
    ),
}
