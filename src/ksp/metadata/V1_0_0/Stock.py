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
	"ModuleAblator",
	"ModuleAeroSurface",
	"ModuleAlternator",
	"ModuleAnalysisResource",
	"ModuleAnchoredDecoupler",
	"ModuleAnimateGeneric",
	"ModuleAnimateHeat",
	"ModuleAnimationGroup",
	"ModuleAsteroid",
	"ModuleAsteroidAnalysis",
	"ModuleAsteroidDrill",
	"ModuleAsteroidInfo",
	"ModuleAsteroidResource",
	"ModuleBiomeScanner",
	"ModuleCargoBay",
	"ModuleCommand",
	"ModuleControlSurface",
	"ModuleDataTransmitter",
	"ModuleDecouple",
	"ModuleDeployableSolarPanel",
	"ModuleDockingNode",
	"ModuleDragModifier",
	"ModuleEngines",
	"ModuleEnginesFX",
	"ModuleEnviroSensor",
	"ModuleFuelJettison",
	"ModuleGPS",
	"ModuleGenerator",
	"ModuleGimbal",
	"ModuleGrappleNode",
	"ModuleHighDefCamera",
	"ModuleJettison",
	"ModuleLandingGear",
	"ModuleLandingGearFixed",
	"ModuleLandingLeg",
	"ModuleLiftingSurface",
	"ModuleLight",
	"ModuleOrbitalScanner",
	"ModuleOrbitalSurveyor",
	"ModuleOverheatDisplay",
	"ModuleParachute",
	"ModuleProceduralFairing",
	"ModuleRCS",
	"ModuleReactionWheel",
	"ModuleResourceConverter",
	"ModuleResourceHarvester",
	"ModuleResourceIntake",
	"ModuleResourceScanner",
	"ModuleSAS",
	"ModuleScienceContainer",
	"ModuleScienceConverter",
	"ModuleScienceExperiment",
	"ModuleScienceLab",
	"ModuleSeeThroughObject",
	"ModuleSteering",
	"ModuleSurfaceFX",
	"ModuleTestSubject",
	"ModuleWheel",
	"MultiModeEngine",
	"RetractableLadder",
])

PARTS_BY_CATEGORY = {
	'*DEPRECATED*': set([
		'elevonMk3'
	]),
	'*UNSORTED*': set([
		'PotatoRoid'
	]),
	'Aero': set([
		'AdvancedCanard', 'CanardController', 'CircularIntake', 'HeatShield1', 'HeatShield2', 'HeatShield3', 'IntakeRadialLong', 'MK1IntakeFuselage', 'R8winglet', 'StandardCtrlSrf'
		'airScoop', 'airbrake1', 'airlinerCtrlSrf', 'airlinerMainWing', 'airlinerTailFin', 'airplaneTail', 'airplaneTailB', 'deltaWing', 'delta_small', 'elevon2'
		'elevon3', 'elevon5', 'fairingSize1', 'fairingSize2', 'fairingSize3', 'nacelleBody', 'noseCone', 'pointyNoseConeA', 'pointyNoseConeB', 'radialEngineBody'
		'ramAirIntake', 'rocketNoseCone', 'shockConeIntake', 'smallCtrlSrf', 'standardNoseCone', 'structuralWing', 'structuralWing2', 'structuralWing3', 'structuralWing4', 'sweptWing'
		'sweptWing1', 'sweptWing2', 'tailfin', 'wingConnector', 'wingConnector2', 'wingConnector3', 'wingConnector4', 'wingConnector5', 'wingShuttleDelta', 'wingShuttleElevon1'
		'wingShuttleElevon2', 'wingShuttleRudder', 'wingShuttleStrake', 'wingStrake', 'winglet', 'winglet3'
	]),
	'Control': set([
		'RCSBlock', 'advSasModule', 'asasmodule1-2', 'avionicsNoseCone', 'linearRcs', 'sasModule', 'vernierEngine'
	]),
	'Engine': set([
		'JetEngine', 'RAPIER', 'engineLargeSkipper', 'ionEngine', 'liquidEngine', 'liquidEngine1-2', 'liquidEngine2', 'liquidEngine2-2', 'liquidEngine3', 'liquidEngineMini'
		'microEngine', 'nuclearEngine', 'omsEngine', 'radialEngineMini', 'radialLiquidEngine1-2', 'sepMotor1', 'smallRadialEngine', 'solidBooster', 'solidBooster1-1', 'solidBooster_sm'
		'toroidalAerospike', 'turboFanEngine'
	]),
	'FuelTank': set([
		'LargeTank', 'MK1Fuselage', 'RCSFuelTank', 'RCSTank1-2', 'SmallTank', 'adapterMk3-Mk2', 'adapterMk3-Size2', 'adapterMk3-Size2Slant', 'adapterSize2-Mk2', 'adapterSize2-Size1'
		'adapterSize2-Size1Slant', 'adapterSize3-Mk3', 'fuelLine', 'fuelTank', 'fuelTank1-2', 'fuelTank2-2', 'fuelTank3-2', 'fuelTank4-2', 'fuelTankSmall', 'fuelTankSmallFlat'
		'fuelTank_long', 'miniFuelTank', 'mk3FuselageLFO_100', 'mk3FuselageLFO_25', 'mk3FuselageLFO_50', 'mk3FuselageLF_100', 'mk3FuselageLF_25', 'mk3FuselageLF_50', 'mk3FuselageMONO', 'radialRCSTank'
		'rcsTankMini', 'rcsTankRadialLong', 'toroidalFuelTank', 'xenonTank', 'xenonTankLarge', 'xenonTankRadial'
	]),
	'Pods': set([
		'Mark1-2Pod', 'Mark1Cockpit', 'Mark2Cockpit', 'cupola', 'landerCabinSmall', 'mk1pod', 'mk2Cockpit_Inline', 'mk2Cockpit_Standard', 'mk2DroneCore', 'mk2LanderCabin'
		'mk3Cockpit_Shuttle', 'probeCoreCube', 'probeCoreHex', 'probeCoreOcto', 'probeCoreOcto2', 'probeCoreSphere', 'probeStackLarge', 'probeStackSmall', 'roverBody', 'seatExternalCmd'
	]),
	'Propulsion': set([
		'MassiveBooster', 'Size2LFB', 'Size3AdvancedEngine', 'Size3EngineCluster', 'Size3LargeTank', 'Size3MediumTank', 'Size3SmallTank', 'mk2Fuselage', 'mk2FuselageLongLFO', 'mk2FuselageShortLFO'
		'mk2FuselageShortLiquid', 'mk2FuselageShortMono', 'mk2SpacePlaneAdapter', 'mk2_1m_AdapterLong', 'mk2_1m_Bicoupler', 'noseConeAdapter'
	]),
	'Science': set([
		'GooExperiment', 'Large_Crewed_Lab', 'OrbitalScanner', 'SurfaceScanner', 'SurveyScanner', 'commDish', 'longAntenna', 'mediumDishAntenna', 'science_module', 'sensorAccelerometer'
		'sensorAtmosphere', 'sensorBarometer', 'sensorGravimeter', 'sensorThermometer'
	]),
	'Structural': set([
		'Mk1FuselageStructural', 'Size3to2Adapter', 'adapterLargeSmallBi', 'adapterLargeSmallQuad', 'adapterLargeSmallTri', 'adapterSmallMiniShort', 'adapterSmallMiniTall', 'decoupler1-2', 'largeAdapter', 'largeAdapter2'
		'launchClamp1', 'radialDecoupler', 'radialDecoupler1-2', 'radialDecoupler2', 'size3Decoupler', 'smallHardpoint', 'stackBiCoupler', 'stackDecoupler', 'stackDecouplerMini', 'stackPoint1'
		'stackQuadCoupler', 'stackSeparator', 'stackSeparatorBig', 'stackSeparatorMini', 'stackTriCoupler', 'stationHub', 'structuralIBeam1', 'structuralIBeam2', 'structuralIBeam3', 'structuralMiniNode'
		'structuralPanel1', 'structuralPanel2', 'structuralPylon', 'strutConnector', 'strutCube', 'strutOcto', 'trussAdapter', 'trussPiece1x', 'trussPiece3x'
	]),
	'Utility': set([
		'FuelCell', 'FuelCellArray', 'GearFixed', 'GearFree', 'GearLarge', 'GearMedium', 'GrapplingDevice', 'ISRU', 'LaunchEscapeSystem', 'RadialDrill'
		'ServiceBay_125', 'ServiceBay_250', 'SmallGearBay', 'batteryBank', 'batteryBankLarge', 'batteryBankMini', 'batteryPack', 'crewCabin', 'dockingPort1', 'dockingPort2'
		'dockingPort3', 'dockingPortLarge', 'dockingPortLateral', 'ksp_r_largeBatteryPack', 'ladder1', 'landingLeg1', 'landingLeg1-2', 'largeSolarPanel', 'miniLandingLeg', 'mk2CargoBayL'
		'mk2CargoBayS', 'mk2CrewCabin', 'mk2DockingPort', 'mk3CargoBayL', 'mk3CargoBayM', 'mk3CargoBayS', 'mk3CrewCabin', 'parachuteDrogue', 'parachuteLarge', 'parachuteRadial'
		'parachuteSingle', 'radialDrogue', 'roverWheel1', 'roverWheel2', 'roverWheel3', 'rtg', 'solarPanels1', 'solarPanels2', 'solarPanels3', 'solarPanels4'
		'solarPanels5', 'spotLight1', 'spotLight2', 'telescopicLadder', 'telescopicLadderBay', 'wheelMed'
	]),
}

from ksp.metadata import sum_all_parts
PARTS = sum_all_parts(PARTS_BY_CATEGORY)

