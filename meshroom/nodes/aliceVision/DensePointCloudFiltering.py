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
            label='Input Mesh',
            description='''Input Mesh (OBJ file format).''',
            value='',
            uid=[0],
        ),

        desc.File(
            name="inputRawSfm",
            label="Raw Dense Point Cloud",
            description="Output dense point cloud with visibilities (SfMData file format).",
            value="{cache}/{nodeType}/{uid0}/densePointCloud_raw.abc",
            uid=[],
        ),

        desc.FloatParam(
            name='radiusFactor',
            label='radiusFactor',
            description='radiusFactor',
            value=1.0,
            range=(0.0, 10.0, 0.1),
            uid=[0],
        ),

        desc.FloatParam(
            name='filterStrength',
            label='Filter Strength',
            description='Filter Strength',
            value=1.0,
            range=(0.0, 10.0, 0.1),
            uid=[0],
        ),

        desc.FloatParam(
            name='epsilonRadius',
            label='Epsilon Radius',
            description='Epsilon Radius',
            value=1.0,
            range=(0.0, 10.0, 0.1),
            uid=[0],
        ),

        desc.IntParam(
            name='iterations',
            label='iterations',
            description='iterations',
            value=1,
            range=(0, 20, 1),
            uid=[0],
        ),
    ]


    outputs = [
        desc.File(
            name="outputMesh",
            label="Output Mesh",
            description="Output mesh (OBJ file format).",
            value="{cache}/{nodeType}/{uid0}/mesh.obj",
            uid=[],
        ),
    ]
