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
	"ModuleWheel",
	"MultiModeEngine",
	"RetractableLadder",
])

PARTS = set([
	'AdvancedCanard', 'CanardController', 'CircularIntake', 'GooExperiment', 'JetEngine', 'Large_Crewed_Lab', 'MK1Fuselage', 'Mark1-2Pod', 'Mark1Cockpit', 'Mark2Cockpit'
	'Mk1FuselageStructural', 'R8winglet', 'RAPIER', 'RCSBlock', 'RCSFuelTank', 'RCSTank1-2', 'SmallGearBay', 'StandardCtrlSrf', 'adapterLargeSmallBi', 'adapterLargeSmallQuad'
	'adapterLargeSmallTri', 'adapterSmallMiniShort', 'adapterSmallMiniTall', 'advSasModule', 'airScoop', 'airplaneTail', 'asasmodule1-2', 'avionicsNoseCone', 'batteryBank', 'batteryBankLarge'
	'batteryBankMini', 'batteryPack', 'commDish', 'crewCabin', 'cupola', 'decoupler1-2', 'deltaWing', 'dockingPort1', 'dockingPort2', 'dockingPort3'
	'dockingPortLarge', 'dockingPortLateral', 'engineLargeSkipper', 'fuelLine', 'fuelTank', 'fuelTank1-2', 'fuelTank2-2', 'fuelTank3-2', 'fuelTank4-2', 'fuelTankSmall'
	'fuelTankSmallFlat', 'fuelTank_long', 'ionEngine', 'ksp_r_largeBatteryPack', 'ladder1', 'landerCabinSmall', 'landingLeg1', 'landingLeg1-2', 'largeAdapter', 'largeAdapter2'
	'largeSolarPanel', 'launchClamp1', 'linearRcs', 'liquidEngine', 'liquidEngine1-2', 'liquidEngine2', 'liquidEngine2-2', 'liquidEngine3', 'liquidEngineMini', 'longAntenna'
	'mark3Cockpit', 'mediumDishAntenna', 'microEngine', 'miniFuelTank', 'miniLandingLeg', 'mk1pod', 'mk2Fuselage', 'mk2LanderCabin', 'mk2SpacePlaneAdapter', 'mk3Fuselage'
	'mk3spacePlaneAdapter', 'nacelleBody', 'noseCone', 'noseConeAdapter', 'nuclearEngine', 'parachuteDrogue', 'parachuteLarge', 'parachuteRadial', 'parachuteSingle', 'probeCoreCube'
	'probeCoreHex', 'probeCoreOcto', 'probeCoreOcto2', 'probeCoreSphere', 'probeStackLarge', 'probeStackSmall', 'radialDecoupler', 'radialDecoupler1-2', 'radialDecoupler2', 'radialEngineBody'
	'radialEngineMini', 'radialLiquidEngine1-2', 'radialRCSTank', 'ramAirIntake', 'rcsTankMini', 'rcsTankRadialLong', 'rocketNoseCone', 'roverBody', 'roverWheel1', 'roverWheel2'
	'roverWheel3', 'rtg', 'sasModule', 'science_module', 'seatExternalCmd', 'sensorAccelerometer', 'sensorBarometer', 'sensorGravimeter', 'sensorThermometer', 'sepMotor1'
	'smallCtrlSrf', 'smallHardpoint', 'smallRadialEngine', 'solarPanels1', 'solarPanels2', 'solarPanels3', 'solarPanels4', 'solarPanels5', 'solidBooster', 'solidBooster1-1'
	'spotLight1', 'spotLight2', 'stackBiCoupler', 'stackDecoupler', 'stackDecouplerMini', 'stackPoint1', 'stackQuadCoupler', 'stackSeparator', 'stackSeparatorBig', 'stackSeparatorMini'
	'stackTriCoupler', 'standardNoseCone', 'stationHub', 'structuralIBeam1', 'structuralIBeam2', 'structuralIBeam3', 'structuralMiniNode', 'structuralPanel1', 'structuralPanel2', 'structuralPylon'
	'structuralWing', 'strutConnector', 'strutCube', 'strutOcto', 'sweptWing', 'tailfin', 'telescopicLadder', 'telescopicLadderBay', 'toroidalAerospike', 'toroidalFuelTank'
	'trussAdapter', 'trussPiece1x', 'trussPiece3x', 'turboFanEngine', 'wheelMed', 'wingConnector', 'winglet', 'winglet3', 'xenonTank', 'xenonTankRadial'
])
