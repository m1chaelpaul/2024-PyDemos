import magicbot
import wpilib
import wpilib.drive  
import phoenix5
from components.drivetrain import Drivetrain
from components.joystick import Joystick

class MyRobot(magicbot.MagicRobot):

    drivetrain: Drivetrain
    joystick: Joystick

    def createObjects(self):
        self.fr_motor = phoenix5.WPI_TalonSRX(55)
        self.fl_motor = phoenix5.WPI_TalonSRX(12)
        self.br_motor = phoenix5.WPI_TalonSRX(15)
        self.bl_motor = phoenix5.WPI_TalonSRX(18)

        self.rightMotors = wpilib.MotorControllerGroup(self.fr_motor, self.br_motor)
        self.leftMotors = wpilib.MotorControllerGroup(self.bl_motor, self.br_motor)
        self.robDrive = wpilib.drive.DifferentialDrive(self.rightMotors, self.leftMotors)
        self.controller = wpilib.Joystick(8)


    def teleopPeriodic(self):
        self.robDrive.arcadeDrive(self.controller.getY(), self.controller.getX())

    