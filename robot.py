import magicbot
import wpilib
import wpilib.drive  
import phoenix5
from components.drivetrain import Drivetrain
from components.controller import Controller
from wpilib import SmartDashboard
import navx

class MyRobot(magicbot.MagicRobot):

    drivetrain: Drivetrain
    controller: Controller

    def createObjects(self):
        self.fr_motor = phoenix5.WPI_TalonSRX(55)
        self.fl_motor = phoenix5.WPI_TalonSRX(12)
        self.br_motor = phoenix5.WPI_TalonSRX(15)
        self.bl_motor = phoenix5.WPI_TalonSRX(18)

        self.rightMotors = wpilib.MotorControllerGroup(self.fr_motor, self.br_motor)
        self.leftMotors = wpilib.MotorControllerGroup(self.bl_motor, self.br_motor)
        self.robDrive = wpilib.drive.DifferentialDrive(self.rightMotors, self.leftMotors)
        self.navx = navx.AHRS.create_spi()
        self.controller = wpilib.Joystick(0)


    def teleopPeriodic(self):
            if self.controller.getTrigger():
                self.controller.turn_to_angle(180)
            else:
                self.drivetrain.arcadeDrive(
                    self.controller.getY() * 0.5, 
                    -self.controller.getX() * 0.5
                )
                
            SmartDashboard.putNumber("JOYSTICK X: ", self.controller.getX())
            SmartDashboard.putBoolean("JOYSTICK Y:", self.controller.getY())
