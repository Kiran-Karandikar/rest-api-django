"""
<-->.
"""

# Python modules
from rest_framework import serializers as szs


# 3rd party Modules
# -N/A

# Project Imports
# -N/A

# Global vars
# -N/A


class HelloSerailzer(szs.Serializer):
    """
    Serialize to serialize the name passed to api view.
    """
    name = szs.CharField(max_length = 10)
