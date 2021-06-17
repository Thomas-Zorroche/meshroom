__version__ = "1.0"

from meshroom.core import desc

import os.path

class DensePointCloudFiltering(desc.CommandLineNode):
    commandLine = 'aliceVision_densePointCloudFiltering {allParams}'

    category = 'Mesh Post-Processing'
    documentation = '''
TODO
'''

    inputs = [
        desc.File(
            name='inputMesh',
            label='Mesh',
            description='''Input Mesh (OBJ file format).''',
            value='',
            uid=[0],
        ),

        desc.File(
            name="output",
            label="Dense SfMData RAW",
            description="Output dense point cloud with visibilities (SfMData file format).",
            value="{cache}/{nodeType}/{uid0}/densePointCloud_raw.abc",
            uid=[],
        ),
    ]


    outputs = [
        desc.File(
            name="outputMesh",
            label="Mesh",
            description="Output mesh (OBJ file format).",
            value="{cache}/{nodeType}/{uid0}/mesh.obj",
            uid=[],
        ),
    ]
