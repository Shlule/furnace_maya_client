from imaplib import Commands

name="furnace_maya_client"
version = "0.0.1"

authors = ["Shlule"]

description ="""
set of python module and maya config to integrate maya in the furnace environement
"""

vcs = "git"

def commands():
    """
    Set the environment variables for silex_maya
    """
    # env.SILEX_ACTION_CONFIG.prepend("{root}/silex_maya/config")
    env.PYTHONPATH.append("{root}")
    env.PYTHONPATH.append("{root}/startup")

    #add location of checkrepository for application found check implemented here
    env.FURNACE_CHECK_CONFIG.append("{root}/furnace_maya_client/checkRepository")
    # env.XBMLANGPATH.append("{root}/startup/icons")

    parser_module = "furnace_maya_client.cli.parser"
    alias("furnace", f"mayapy -m {parser_module}")

@late()
def requires():
    # major = str(this.version.major)
    furnace_requirement = ["furnace_python_client"]
    # if major in ["dev", "beta", "prod"]:
        # furnace_requirement = [f"furnace_python_client-{major}"]

    return ["maya"] + furnace_requirement