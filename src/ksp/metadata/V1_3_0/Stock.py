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
	"FlagSite",
	"KerbalEVA",
	"KerbalSeat",
	"LaunchClamp",
	"ModuleAblator",
	"ModuleActiveRadiator",
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
	"ModuleColorChanger",
	"ModuleCommand",
	"ModuleConductionMultiplier",
	"ModuleControlSurface",
	"ModuleCoreHeat",
	"ModuleDataTransmitter",
	"ModuleDecouple",
	"ModuleDeployableAntenna",
	"ModuleDeployableRadiator",
	"ModuleDeployableSolarPanel",
	"ModuleDockingNode",
	"ModuleDragModifier",
	"ModuleEngines",
	"ModuleEnginesFX",
	"ModuleEnviroSensor",
	"ModuleExperienceManagement",
	"ModuleFuelJettison",
	"ModuleGPS",
	"ModuleGenerator",
	"ModuleGimbal",
	"ModuleGrappleNode",
	"ModuleJettison",
	"ModuleKerbNetAccess",
	"ModuleLiftingSurface",
	"ModuleLight",
	"ModuleOrbitalScanner",
	"ModuleOrbitalSurveyor",
	"ModuleOverheatDisplay",
	"ModuleParachute",
	"ModuleProbeControlPoint",
	"ModuleProceduralFairing",
	"ModuleRCSFX",
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
	"ModuleStatusLight",
	"ModuleStructuralNode",
	"ModuleStructuralNodeToggle",
	"ModuleSurfaceFX",
	"ModuleTestSubject",
	"ModuleToggleCrossfeed",
	"ModuleTripLogger",
	"ModuleWheelBase",
	"ModuleWheelBogey",
	"ModuleWheelBrakes",
	"ModuleWheelDamage",
	"ModuleWheelDeployment",
	"ModuleWheelLock",
	"ModuleWheelMotor",
	"ModuleWheelMotorSteering",
	"ModuleWheelSteering",
	"ModuleWheelSuspension",
	"MultiModeEngine",
	"RetractableLadder",
	"SentinelModule",
])

PARTS_BY_CATEGORY = {
	'*UNSORTED*': set([
		'PotatoRoid', 'flag', 'kerbalEVA', 'kerbalEVAfemale'
	]),
	'Aero': set([
		'AdvancedCanard', 'CanardController', 'CircularIntake', 'IntakeRadialLong', 'MK1IntakeFuselage', 'R8winglet', 'StandardCtrlSrf', 'airScoop', 'airbrake1', 'airlinerCtrlSrf'
		'airlinerMainWing', 'airlinerTailFin', 'airplaneTail', 'airplaneTailB', 'basicFin', 'deltaWing', 'delta_small', 'elevon2', 'elevon3', 'elevon5'
		'miniIntake', 'nacelleBody', 'noseCone', 'pointyNoseConeA', 'pointyNoseConeB', 'radialEngineBody', 'ramAirIntake', 'rocketNoseCone', 'shockConeIntake', 'smallCtrlSrf'
		'standardNoseCone', 'structuralWing', 'structuralWing2', 'structuralWing3', 'structuralWing4', 'sweptWing', 'sweptWing1', 'sweptWing2', 'tailfin', 'wingConnector'
		'wingConnector2', 'wingConnector3', 'wingConnector4', 'wingConnector5', 'wingShuttleDelta', 'wingShuttleElevon1', 'wingShuttleElevon2', 'wingShuttleRudder', 'wingShuttleStrake', 'wingStrake'
		'winglet', 'winglet3'
	]),
	'Communication': set([
		'HighGainAntenna', 'HighGainAntenna5', 'RelayAntenna100', 'RelayAntenna5', 'RelayAntenna50', 'SurfAntenna', 'commDish', 'longAntenna', 'mediumDishAntenna'
	]),
	'Control': set([
		'RCSBlock', 'advSasModule', 'asasmodule1-2', 'avionicsNoseCone', 'linearRcs', 'sasModule', 'vernierEngine'
	]),
	'Coupling': set([
		'GrapplingDevice', 'decoupler1-2', 'dockingPort1', 'dockingPort2', 'dockingPort3', 'dockingPortLarge', 'dockingPortLateral', 'mk2DockingPort', 'radialDecoupler', 'radialDecoupler1-2'
		'radialDecoupler2', 'size3Decoupler', 'stackDecoupler', 'stackDecouplerMini', 'stackSeparator', 'stackSeparatorBig', 'stackSeparatorMini'
	]),
	'Electrical': set([
		'FuelCell', 'FuelCellArray', 'LgRadialSolarPanel', 'batteryBank', 'batteryBankLarge', 'batteryBankMini', 'batteryPack', 'ksp_r_largeBatteryPack', 'largeSolarPanel', 'rtg'
		'solarPanels1', 'solarPanels2', 'solarPanels3', 'solarPanels4', 'solarPanels5'
	]),
	'Engine': set([
		'JetEngine', 'RAPIER', 'engineLargeSkipper', 'ionEngine', 'liquidEngine', 'liquidEngine1-2', 'liquidEngine2', 'liquidEngine2-2', 'liquidEngine3', 'liquidEngineMini'
		'microEngine', 'miniJetEngine', 'nuclearEngine', 'omsEngine', 'radialEngineMini', 'radialLiquidEngine1-2', 'sepMotor1', 'smallRadialEngine', 'solidBooster', 'solidBooster1-1'
		'solidBooster_sm', 'toroidalAerospike', 'turboFanEngine', 'turboFanSize2', 'turboJet'
	]),
	'FuelTank': set([
		'LargeTank', 'MK1Fuselage', 'RCSFuelTank', 'RCSTank1-2', 'RadialOreTank', 'SmallTank', 'adapterMk3-Mk2', 'adapterMk3-Size2', 'adapterMk3-Size2Slant', 'adapterSize2-Mk2'
		'adapterSize2-Size1', 'adapterSize2-Size1Slant', 'adapterSize3-Mk3', 'fuelLine', 'fuelTank', 'fuelTank1-2', 'fuelTank2-2', 'fuelTank3-2', 'fuelTank4-2', 'fuelTankSmall'
		'fuelTankSmallFlat', 'fuelTank_long', 'miniFuelTank', 'mk3FuselageLFO_100', 'mk3FuselageLFO_25', 'mk3FuselageLFO_50', 'mk3FuselageLF_100', 'mk3FuselageLF_25', 'mk3FuselageLF_50', 'mk3FuselageMONO'
		'radialRCSTank', 'rcsTankMini', 'rcsTankRadialLong', 'toroidalFuelTank', 'xenonTank', 'xenonTankLarge', 'xenonTankRadial'
	]),
	'Ground': set([
		'GearFixed', 'GearFree', 'GearLarge', 'GearMedium', 'GearSmall', 'SmallGearBay', 'landingLeg1', 'landingLeg1-2', 'miniLandingLeg', 'roverWheel1'
		'roverWheel2', 'roverWheel3', 'wheelMed'
	]),
	'Payload': set([
		'ServiceBay_125', 'ServiceBay_250', 'fairingSize1', 'fairingSize2', 'fairingSize3', 'mk2CargoBayL', 'mk2CargoBayS', 'mk3CargoBayL', 'mk3CargoBayM', 'mk3CargoBayS'
		'mk3CargoRamp'
	]),
	'Pods': set([
		'HECS2_ProbeCore', 'Mark1-2Pod', 'Mark1Cockpit', 'Mark2Cockpit', 'cupola', 'landerCabinSmall', 'mk1pod', 'mk2Cockpit_Inline', 'mk2Cockpit_Standard', 'mk2DroneCore'
		'mk2LanderCabin', 'mk3Cockpit_Shuttle', 'probeCoreCube', 'probeCoreHex', 'probeCoreOcto', 'probeCoreOcto2', 'probeCoreSphere', 'probeStackLarge', 'probeStackSmall', 'roverBody'
		'seatExternalCmd'
	]),
	'Propulsion': set([
		'MassiveBooster', 'SSME', 'Size2LFB', 'Size3AdvancedEngine', 'Size3EngineCluster', 'Size3LargeTank', 'Size3MediumTank', 'Size3SmallTank', 'miniFuselage', 'mk2Fuselage'
		'mk2FuselageLongLFO', 'mk2FuselageShortLFO', 'mk2FuselageShortLiquid', 'mk2FuselageShortMono', 'mk2SpacePlaneAdapter', 'mk2_1m_AdapterLong', 'mk2_1m_Bicoupler', 'noseConeAdapter'
	]),
	'Science': set([
		'GooExperiment', 'InfraredTelescope', 'Large_Crewed_Lab', 'OrbitalScanner', 'ScienceBox', 'SurfaceScanner', 'SurveyScanner', 'science_module', 'sensorAccelerometer', 'sensorAtmosphere'
		'sensorBarometer', 'sensorGravimeter', 'sensorThermometer'
	]),
	'Structural': set([
		'Mk1FuselageStructural', 'Size3to2Adapter', 'adapterEngines', 'adapterLargeSmallBi', 'adapterLargeSmallQuad', 'adapterLargeSmallTri', 'adapterSmallMiniShort', 'adapterSmallMiniTall', 'largeAdapter', 'largeAdapter2'
		'launchClamp1', 'smallHardpoint', 'stackBiCoupler', 'stackPoint1', 'stackQuadCoupler', 'stackTriCoupler', 'stationHub', 'structuralIBeam1', 'structuralIBeam2', 'structuralIBeam3'
		'structuralMiniNode', 'structuralPanel1', 'structuralPanel2', 'structuralPylon', 'strutConnector', 'strutCube', 'strutOcto', 'trussAdapter', 'trussPiece1x', 'trussPiece3x'
	]),
	'Thermal': set([
		'HeatShield0', 'HeatShield1', 'HeatShield2', 'HeatShield3', 'InflatableHeatShield', 'foldingRadLarge', 'foldingRadMed', 'foldingRadSmall', 'radPanelEdge', 'radPanelLg'
		'radPanelSm'
	]),
	'Utility': set([
		'ISRU', 'LaunchEscapeSystem', 'MK1CrewCabin', 'MiniDrill', 'MiniISRU', 'RadialDrill', 'crewCabin', 'ladder1', 'mk2CrewCabin', 'mk3CrewCabin'
		'parachuteDrogue', 'parachuteLarge', 'parachuteRadial', 'parachuteSingle', 'radialDrogue', 'spotLight1', 'spotLight2', 'telescopicLadder', 'telescopicLadderBay'
	]),
}

from itertools import chain
PARTS = set(chain.from_iterable(PARTS_BY_CATEGORY.values()))

