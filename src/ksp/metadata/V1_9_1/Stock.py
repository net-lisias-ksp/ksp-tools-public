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
	"FXModuleAnimateRCS",
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
	"ModuleDynamicNodes",          # Not used by Stock, but by MH & Serenity
	"ModuleEngines",
	"ModuleEnginesFX",
	"ModuleEnviroSensor",
	"ModuleEvaChute",
	"ModuleExperienceManagement",
	"ModuleFuelJettison",
	"ModuleGPS",
	"ModuleGenerator",
	"ModuleGimbal",
	"ModuleGrappleNode",
	"ModuleInventoryPart",
	"ModuleJettison",
	"ModuleKerbNetAccess",
	"ModuleLiftingSurface",
	"ModuleLight",
	"ModuleOrbitalScanner",
	"ModuleOrbitalSurveyor",
	"ModuleOverheatDisplay",
	"ModuleParachute",
	"ModulePartVariants",
	"ModuleProbeControlPoint",
	"ModuleProceduralFairing",
	"ModuleRCSFX",
	"ModuleReactionWheel",
	"ModuleResourceConverter",
	"ModuleResourceDrain",
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
	'*DEPRECATED*': set([
		'RCSBlock', 'ServiceBay_125', 'ServiceBay_250', 'Size3to2Adapter', 'engineLargeSkipper', 'liquidEngine1-2', 'liquidEngine2-2', 'liquidEngine3', 'liquidEngineMini', 'microEngine'
		'mk1pod', 'mk2LanderCabin', 'probeCoreHex', 'probeCoreOcto', 'probeCoreOcto2', 'probeCoreSphere', 'radialEngineMini', 'rocketNoseCone', 'roverBody', 'smallRadialEngine'
		'solidBooster', 'solidBooster_sm', 'stackBiCoupler', 'stackTriCoupler'
	]),
	'*UNSORTED*': set([
		'PotatoRoid', 'flag', 'kerbalEVA', 'kerbalEVAfemale'
	]),
	'Aero': set([
		'AdvancedCanard', 'CanardController', 'CircularIntake', 'IntakeRadialLong', 'MK1IntakeFuselage', 'R8winglet', 'StandardCtrlSrf', 'airScoop', 'airbrake1', 'airlinerCtrlSrf'
		'airlinerMainWing', 'airlinerTailFin', 'airplaneTail', 'airplaneTailB', 'basicFin', 'deltaWing', 'delta_small', 'elevon2', 'elevon3', 'elevon5'
		'miniIntake', 'nacelleBody', 'noseCone', 'pointyNoseConeA', 'pointyNoseConeB', 'radialEngineBody', 'ramAirIntake', 'rocketNoseConeSize3', 'rocketNoseCone_v2', 'shockConeIntake'
		'smallCtrlSrf', 'standardNoseCone', 'structuralWing', 'structuralWing2', 'structuralWing3', 'structuralWing4', 'sweptWing', 'sweptWing1', 'sweptWing2', 'tailfin'
		'wingConnector', 'wingConnector2', 'wingConnector3', 'wingConnector4', 'wingConnector5', 'wingShuttleDelta', 'wingShuttleElevon1', 'wingShuttleElevon2', 'wingShuttleRudder', 'wingShuttleStrake'
		'wingStrake', 'winglet', 'winglet3'
	]),
	'Communication': set([
		'HighGainAntenna', 'HighGainAntenna5', 'RelayAntenna100', 'RelayAntenna5', 'RelayAntenna50', 'SurfAntenna', 'commDish', 'longAntenna', 'mediumDishAntenna'
	]),
	'Control': set([
		'RCSBlock_v2', 'advSasModule', 'asasmodule1-2', 'avionicsNoseCone', 'linearRcs', 'sasModule', 'vernierEngine'
	]),
	'Coupling': set([
		'Decoupler_0', 'Decoupler_1', 'Decoupler_2', 'Decoupler_3', 'GrapplingDevice', 'Separator_0', 'Separator_1', 'Separator_2', 'Separator_3', 'dockingPort1'
		'dockingPort2', 'dockingPort3', 'dockingPortLarge', 'dockingPortLateral', 'mk2DockingPort', 'radialDecoupler', 'radialDecoupler1-2', 'radialDecoupler2'
	]),
	'Electrical': set([
		'FuelCell', 'FuelCellArray', 'LgRadialSolarPanel', 'batteryBank', 'batteryBankLarge', 'batteryBankMini', 'batteryPack', 'ksp_r_largeBatteryPack', 'largeSolarPanel', 'rtg'
		'solarPanels1', 'solarPanels2', 'solarPanels3', 'solarPanels4', 'solarPanels5'
	]),
	'Engine': set([
		'Clydesdale', 'JetEngine', 'MassiveBooster', 'Mite', 'RAPIER', 'SSME', 'Shrimp', 'Size2LFB', 'Size3AdvancedEngine', 'Size3EngineCluster'
		'Thoroughbred', 'engineLargeSkipper_v2', 'ionEngine', 'liquidEngine', 'liquidEngine2', 'liquidEngine2-2_v2', 'liquidEngine3_v2', 'liquidEngineMainsail_v2', 'liquidEngineMini_v2', 'microEngine_v2'
		'miniJetEngine', 'nuclearEngine', 'omsEngine', 'radialEngineMini_v2', 'radialLiquidEngine1-2', 'sepMotor1', 'smallRadialEngine_v2', 'solidBooster1-1', 'solidBooster_sm_v2', 'solidBooster_v2'
		'toroidalAerospike', 'turboFanEngine', 'turboFanSize2', 'turboJet'
	]),
	'FuelTank': set([
		'LargeTank', 'MK1Fuselage', 'RCSFuelTank', 'RCSTank1-2', 'RadialOreTank', 'ReleaseValve', 'Rockomax16_BW', 'Rockomax32_BW', 'Rockomax64_BW', 'Rockomax8BW'
		'Size3To2Adapter_v2', 'SmallTank', 'adapterMk3-Mk2', 'adapterMk3-Size2', 'adapterMk3-Size2Slant', 'adapterSize2-Mk2', 'adapterSize2-Size1', 'adapterSize2-Size1Slant', 'adapterSize3-Mk3', 'externalTankToroid'
		'fuelLine', 'fuelTank', 'fuelTankSmall', 'fuelTankSmallFlat', 'fuelTank_long', 'miniFuelTank', 'mk3FuselageLFO_100', 'mk3FuselageLFO_25', 'mk3FuselageLFO_50', 'mk3FuselageLF_100'
		'mk3FuselageLF_25', 'mk3FuselageLF_50', 'mk3FuselageMONO', 'radialRCSTank', 'rcsTankMini', 'rcsTankRadialLong', 'xenonTank', 'xenonTankLarge', 'xenonTankRadial'
	]),
	'Ground': set([
		'GearFixed', 'GearFree', 'GearLarge', 'GearMedium', 'GearSmall', 'SmallGearBay', 'landingLeg1', 'landingLeg1-2', 'miniLandingLeg', 'roverWheel1'
		'roverWheel2', 'roverWheel3', 'wheelMed'
	]),
	'Payload': set([
		'ServiceBay_125_v2', 'ServiceBay_250_v2', 'fairingSize1', 'fairingSize2', 'fairingSize3', 'mk2CargoBayL', 'mk2CargoBayS', 'mk3CargoBayL', 'mk3CargoBayM', 'mk3CargoBayS'
		'mk3CargoRamp'
	]),
	'Pods': set([
		'HECS2_ProbeCore', 'Mark1Cockpit', 'Mark2Cockpit', 'cupola', 'landerCabinSmall', 'mk1-3pod', 'mk1pod_v2', 'mk2Cockpit_Inline', 'mk2Cockpit_Standard', 'mk2DroneCore'
		'mk2LanderCabin_v2', 'mk3Cockpit_Shuttle', 'probeCoreCube', 'probeCoreHex_v2', 'probeCoreOcto2_v2', 'probeCoreOcto_v2', 'probeCoreSphere_v2', 'probeStackLarge', 'probeStackSmall', 'roverBody_v2'
		'seatExternalCmd'
	]),
	'Propulsion': set([
		'Size3LargeTank', 'Size3MediumTank', 'Size3SmallTank', 'externalTankCapsule', 'externalTankRound', 'miniFuselage', 'mk2Fuselage', 'mk2FuselageLongLFO', 'mk2FuselageShortLFO', 'mk2FuselageShortLiquid'
		'mk2FuselageShortMono', 'mk2SpacePlaneAdapter', 'mk2_1m_AdapterLong', 'mk2_1m_Bicoupler', 'noseConeAdapter'
	]),
	'Science': set([
		'GooExperiment', 'InfraredTelescope', 'Large_Crewed_Lab', 'OrbitalScanner', 'ScienceBox', 'SurfaceScanner', 'SurveyScanner', 'science_module', 'sensorAccelerometer', 'sensorAtmosphere'
		'sensorBarometer', 'sensorGravimeter', 'sensorThermometer'
	]),
	'Structural': set([
		'Mk1FuselageStructural', 'adapterEngines', 'adapterLargeSmallBi', 'adapterLargeSmallQuad', 'adapterLargeSmallTri', 'adapterSmallMiniShort', 'adapterSmallMiniTall', 'largeAdapter', 'largeAdapter2', 'launchClamp1'
		'smallHardpoint', 'stackBiCoupler_v2', 'stackPoint1', 'stackQuadCoupler', 'stackTriCoupler_v2', 'stationHub', 'structuralIBeam1', 'structuralIBeam2', 'structuralIBeam3', 'structuralMiniNode'
		'structuralPanel1', 'structuralPanel2', 'structuralPylon', 'strutConnector', 'strutCube', 'strutOcto', 'trussAdapter', 'trussPiece1x', 'trussPiece3x'
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

from ksp.metadata import sum_all_parts
PARTS = sum_all_parts(PARTS_BY_CATEGORY)
DEPRECATED_PARTS = set(PARTS_BY_CATEGORY['*DEPRECATED*']) if '*DEPRECATED*' in PARTS_BY_CATEGORY else set()
