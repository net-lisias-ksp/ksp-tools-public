#    This file is part of KSP Tools
#    © 2020 LisiasT
#
#    KSP Tools is licensed as follows:
#
#        * GPL 2.0 : https://www.gnu.org/licenses/gpl-2.0.txt
#
#    KSP Tools is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#
#    You should have received a copy of the GNU General Public License 2.0
#    along with KSP Tools, if not see <https://www.gnu.org/licenses/>.
#
'''
Created on Sep 27, 2020

@author: lisias
'''

MODULES = set([
	"CModuleFuelLine",
	"CModuleLinkedMesh",
	"CModuleStrut",
	"FXModuleAnimateThrottle",
	"FXModuleConstrainPosition",
	"FXModuleLookAtConstraint",
	"FlagDecal",
	"KerbalSeat",
	"LaunchClamp",
	"ModuleAlternator",
	"ModuleAnchoredDecoupler",
	"ModuleAnimateGeneric",
	"ModuleAnimateHeat",
	"ModuleCommand",
	"ModuleControlSurface",
	"ModuleDataTransmitter",
	"ModuleDecouple",
	"ModuleDeployableSolarPanel",
	"ModuleDockingNode",
	"ModuleEngines",
	"ModuleEnginesFX",
	"ModuleEnviroSensor",
	"ModuleGenerator",
	"ModuleGimbal",
	"ModuleJettison",
	"ModuleLandingGear",
	"ModuleLandingLeg",
	"ModuleLight",
	"ModuleParachute",
	"ModuleRCS",
	"ModuleReactionWheel",
	"ModuleResourceIntake",
	"ModuleSAS",
	"ModuleScienceContainer",
	"ModuleScienceExperiment",
	"ModuleScienceLab",
	"ModuleSteering",
	"ModuleTestSubject",
	"ModuleWheel",
	"MultiModeEngine",
	"RetractableLadder",
])

PARTS_BY_CATEGORY = {
	'Aero': set([
		'AdvancedCanard', 'CanardController', 'CircularIntake', 'MK1IntakeFuselage', 'R8winglet', 'airScoop', 'airplaneTail', 'nacelleBody', 'noseCone', 'radialEngineBody'
		'ramAirIntake', 'rocketNoseCone', 'standardNoseCone', 'sweptWing', 'tailfin', 'winglet', 'winglet3'
	]),
	'Control': set([
		'RCSBlock', 'advSasModule', 'asasmodule1-2', 'linearRcs', 'sasModule', 'vernierEngine'
	]),
	'Engine': set([
		'JetEngine', 'RAPIER', 'engineLargeSkipper', 'ionEngine', 'liquidEngine', 'liquidEngine1-2', 'liquidEngine2', 'liquidEngine2-2', 'liquidEngine3', 'liquidEngineMini'
		'microEngine', 'nuclearEngine', 'omsEngine', 'radialEngineMini', 'radialLiquidEngine1-2', 'sepMotor1', 'smallRadialEngine', 'solidBooster', 'solidBooster1-1', 'toroidalAerospike'
		'turboFanEngine'
	]),
	'FuelTank': set([
		'MK1Fuselage', 'RCSFuelTank', 'RCSTank1-2', 'adapterMk3-Mk2', 'adapterMk3-Size2', 'adapterMk3-Size2Slant', 'adapterSize2-Mk2', 'adapterSize2-Size1', 'adapterSize2-Size1Slant', 'adapterSize3-Mk3'
		'fuelLine', 'fuelTank', 'fuelTank1-2', 'fuelTank2-2', 'fuelTank3-2', 'fuelTank4-2', 'fuelTankSmall', 'fuelTankSmallFlat', 'fuelTank_long', 'miniFuelTank'
		'mk3FuselageLFO_100', 'mk3FuselageLFO_25', 'mk3FuselageLFO_50', 'mk3FuselageLF_100', 'mk3FuselageLF_25', 'mk3FuselageLF_50', 'mk3FuselageMONO', 'radialRCSTank', 'rcsTankMini', 'rcsTankRadialLong'
		'toroidalFuelTank', 'xenonTank', 'xenonTankRadial'
	]),
	'Pods': set([
		'Mark1-2Pod', 'Mark1Cockpit', 'Mark2Cockpit', 'cupola', 'landerCabinSmall', 'mk1pod', 'mk2LanderCabin', 'mk3Cockpit_Shuttle', 'probeCoreCube', 'probeCoreHex'
		'probeCoreOcto', 'probeCoreOcto2', 'probeCoreSphere', 'probeStackLarge', 'probeStackSmall', 'seatExternalCmd'
	]),
	'Science': set([
		'GooExperiment', 'Large_Crewed_Lab', 'avionicsNoseCone', 'commDish', 'longAntenna', 'mediumDishAntenna', 'science_module', 'sensorAccelerometer', 'sensorBarometer', 'sensorGravimeter'
		'sensorThermometer'
	]),
	'Structural': set([
		'Mk1FuselageStructural', 'adapterLargeSmallBi', 'adapterLargeSmallQuad', 'adapterLargeSmallTri', 'adapterSmallMiniShort', 'adapterSmallMiniTall', 'decoupler1-2', 'largeAdapter', 'largeAdapter2', 'launchClamp1'
		'noseConeAdapter', 'radialDecoupler', 'radialDecoupler1-2', 'radialDecoupler2', 'roverBody', 'smallHardpoint', 'stackBiCoupler', 'stackDecoupler', 'stackDecouplerMini', 'stackPoint1'
		'stackQuadCoupler', 'stackSeparator', 'stackSeparatorBig', 'stackSeparatorMini', 'stackTriCoupler', 'stationHub', 'structuralIBeam1', 'structuralIBeam2', 'structuralIBeam3', 'structuralMiniNode'
		'structuralPanel1', 'structuralPanel2', 'structuralPylon', 'strutConnector', 'strutCube', 'strutOcto', 'trussAdapter', 'trussPiece1x', 'trussPiece3x'
	]),
	'Utility': set([
		'SmallGearBay', 'batteryBank', 'batteryBankLarge', 'batteryBankMini', 'batteryPack', 'crewCabin', 'dockingPort1', 'dockingPort2', 'dockingPort3', 'dockingPortLarge'
		'dockingPortLateral', 'ksp_r_largeBatteryPack', 'ladder1', 'landingLeg1', 'landingLeg1-2', 'largeSolarPanel', 'miniLandingLeg', 'mk3CargoBayL', 'mk3CargoBayM', 'mk3CargoBayS'
		'mk3CrewCabin', 'parachuteDrogue', 'parachuteLarge', 'parachuteRadial', 'parachuteSingle', 'roverWheel1', 'roverWheel2', 'roverWheel3', 'rtg', 'solarPanels1'
		'solarPanels2', 'solarPanels3', 'solarPanels4', 'solarPanels5', 'spotLight1', 'spotLight2', 'telescopicLadder', 'telescopicLadderBay', 'wheelMed'
	]),
}

from ksp.metadata import sum_all_parts
PARTS = sum_all_parts(PARTS_BY_CATEGORY)
DEPRECATED_PARTS = set(PARTS_BY_CATEGORY['*DEPRECATED*']) if '*DEPRECATED*' in PARTS_BY_CATEGORY else set()
