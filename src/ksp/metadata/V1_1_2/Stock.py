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
	"ModuleCommand",
	"ModuleConductionMultiplier",
	"ModuleControlSurface",
	"ModuleCoreHeat",
	"ModuleDataTransmitter",
	"ModuleDecouple",
	"ModuleDeployableRadiator",
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
	"ModuleStatusLight",
	"ModuleSurfaceFX",
	"ModuleTestSubject",
	"ModuleToggleCrossfeed",
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
])

PARTS = set([
	'AdvancedCanard', 'CanardController', 'CircularIntake', 'FuelCell', 'FuelCellArray', 'GearFixed', 'GearFree', 'GearLarge', 'GearMedium', 'GearSmall'
	'GooExperiment', 'GrapplingDevice', 'HECS2_ProbeCore', 'HeatShield1', 'HeatShield2', 'HeatShield3', 'HighGainAntenna', 'ISRU', 'InflatableHeatShield', 'IntakeRadialLong'
	'JetEngine', 'LargeTank', 'Large_Crewed_Lab', 'LaunchEscapeSystem', 'LgRadialSolarPanel', 'MK1CrewCabin', 'MK1Fuselage', 'MK1IntakeFuselage', 'Mark1-2Pod', 'Mark1Cockpit'
	'Mark2Cockpit', 'MassiveBooster', 'MiniDrill', 'MiniISRU', 'Mk1FuselageStructural', 'OrbitalScanner', 'PotatoRoid', 'R8winglet', 'RAPIER', 'RCSBlock'
	'RCSFuelTank', 'RCSTank1-2', 'RadialDrill', 'RadialOreTank', 'SSME', 'ServiceBay_125', 'ServiceBay_250', 'Size2LFB', 'Size3AdvancedEngine', 'Size3EngineCluster'
	'Size3LargeTank', 'Size3MediumTank', 'Size3SmallTank', 'Size3to2Adapter', 'SmallGearBay', 'SmallTank', 'StandardCtrlSrf', 'SurfaceScanner', 'SurveyScanner', 'adapterEngines'
	'adapterLargeSmallBi', 'adapterLargeSmallQuad', 'adapterLargeSmallTri', 'adapterMk3-Mk2', 'adapterMk3-Size2', 'adapterMk3-Size2Slant', 'adapterSize2-Mk2', 'adapterSize2-Size1', 'adapterSize2-Size1Slant', 'adapterSize3-Mk3'
	'adapterSmallMiniShort', 'adapterSmallMiniTall', 'advSasModule', 'airScoop', 'airbrake1', 'airlinerCtrlSrf', 'airlinerMainWing', 'airlinerTailFin', 'airplaneTail', 'airplaneTailB'
	'asasmodule1-2', 'avionicsNoseCone', 'basicFin', 'batteryBank', 'batteryBankLarge', 'batteryBankMini', 'batteryPack', 'commDish', 'crewCabin', 'cupola'
	'decoupler1-2', 'deltaWing', 'delta_small', 'dockingPort1', 'dockingPort2', 'dockingPort3', 'dockingPortLarge', 'dockingPortLateral', 'elevon2', 'elevon3'
	'elevon5', 'engineLargeSkipper', 'fairingSize1', 'fairingSize2', 'fairingSize3', 'foldingRadLarge', 'foldingRadMed', 'foldingRadSmall', 'fuelLine', 'fuelTank'
	'fuelTank1-2', 'fuelTank2-2', 'fuelTank3-2', 'fuelTank4-2', 'fuelTankSmall', 'fuelTankSmallFlat', 'fuelTank_long', 'ionEngine', 'ksp_r_largeBatteryPack', 'ladder1'
	'landerCabinSmall', 'landingLeg1', 'landingLeg1-2', 'largeAdapter', 'largeAdapter2', 'largeSolarPanel', 'launchClamp1', 'linearRcs', 'liquidEngine', 'liquidEngine1-2'
	'liquidEngine2', 'liquidEngine2-2', 'liquidEngine3', 'liquidEngineMini', 'longAntenna', 'mediumDishAntenna', 'microEngine', 'miniFuelTank', 'miniFuselage', 'miniIntake'
	'miniJetEngine', 'miniLandingLeg', 'mk1pod', 'mk2CargoBayL', 'mk2CargoBayS', 'mk2Cockpit_Inline', 'mk2Cockpit_Standard', 'mk2CrewCabin', 'mk2DockingPort', 'mk2DroneCore'
	'mk2Fuselage', 'mk2FuselageLongLFO', 'mk2FuselageShortLFO', 'mk2FuselageShortLiquid', 'mk2FuselageShortMono', 'mk2LanderCabin', 'mk2SpacePlaneAdapter', 'mk2_1m_AdapterLong', 'mk2_1m_Bicoupler', 'mk3CargoBayL'
	'mk3CargoBayM', 'mk3CargoBayS', 'mk3CargoRamp', 'mk3Cockpit_Shuttle', 'mk3CrewCabin', 'mk3FuselageLFO_100', 'mk3FuselageLFO_25', 'mk3FuselageLFO_50', 'mk3FuselageLF_100', 'mk3FuselageLF_25'
	'mk3FuselageLF_50', 'mk3FuselageMONO', 'nacelleBody', 'noseCone', 'noseConeAdapter', 'nuclearEngine', 'omsEngine', 'parachuteDrogue', 'parachuteLarge', 'parachuteRadial'
	'parachuteSingle', 'pointyNoseConeA', 'pointyNoseConeB', 'probeCoreCube', 'probeCoreHex', 'probeCoreOcto', 'probeCoreOcto2', 'probeCoreSphere', 'probeStackLarge', 'probeStackSmall'
	'radPanelEdge', 'radPanelLg', 'radPanelSm', 'radialDecoupler', 'radialDecoupler1-2', 'radialDecoupler2', 'radialDrogue', 'radialEngineBody', 'radialEngineMini', 'radialLiquidEngine1-2'
	'radialRCSTank', 'ramAirIntake', 'rcsTankMini', 'rcsTankRadialLong', 'rocketNoseCone', 'roverBody', 'roverWheel1', 'roverWheel2', 'roverWheel3', 'rtg'
	'sasModule', 'science_module', 'seatExternalCmd', 'sensorAccelerometer', 'sensorAtmosphere', 'sensorBarometer', 'sensorGravimeter', 'sensorThermometer', 'sepMotor1', 'shockConeIntake'
	'size3Decoupler', 'smallCtrlSrf', 'smallHardpoint', 'smallRadialEngine', 'solarPanels1', 'solarPanels2', 'solarPanels3', 'solarPanels4', 'solarPanels5', 'solidBooster'
	'solidBooster1-1', 'solidBooster_sm', 'spotLight1', 'spotLight2', 'stackBiCoupler', 'stackDecoupler', 'stackDecouplerMini', 'stackPoint1', 'stackQuadCoupler', 'stackSeparator'
	'stackSeparatorBig', 'stackSeparatorMini', 'stackTriCoupler', 'standardNoseCone', 'stationHub', 'structuralIBeam1', 'structuralIBeam2', 'structuralIBeam3', 'structuralMiniNode', 'structuralPanel1'
	'structuralPanel2', 'structuralPylon', 'structuralWing', 'structuralWing2', 'structuralWing3', 'structuralWing4', 'strutConnector', 'strutCube', 'strutOcto', 'sweptWing'
	'sweptWing1', 'sweptWing2', 'tailfin', 'telescopicLadder', 'telescopicLadderBay', 'toroidalAerospike', 'toroidalFuelTank', 'trussAdapter', 'trussPiece1x', 'trussPiece3x'
	'turboFanEngine', 'turboFanSize2', 'turboJet', 'vernierEngine', 'wheelMed', 'wingConnector', 'wingConnector2', 'wingConnector3', 'wingConnector4', 'wingConnector5'
	'wingShuttleDelta', 'wingShuttleElevon1', 'wingShuttleElevon2', 'wingShuttleRudder', 'wingShuttleStrake', 'wingStrake', 'winglet', 'winglet3', 'xenonTank', 'xenonTankLarge'
	'xenonTankRadial'
])
