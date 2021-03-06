# -*- coding: utf-8 -*-
"""
/***************************************************************************
 LatLongCalc
                                 A QGIS plugin
 Permite realizar una conversion entre latitud y longitud entre grados decimales y GMS
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2021-05-03
        copyright            : (C) 2021 by hector sosa
        email                : hososa@unah.hn
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load LatLongCalc class from file LatLongCalc.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .latlongcalc import LatLongCalc
    return LatLongCalc(iface)
