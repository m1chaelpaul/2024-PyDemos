import wpilib
import wpilib.drive
import phoenix5

class MyRobot(wpilib.TimedRobot):
    
    def robotInit(self):
        #declare and itialize motors and joystick
        self.fr_motor = phoenix5.WPI_TalonSRX(55)
        self.fl_motor = phoenix5.WPI_TalonSRX(12)
        self.br_motor = phoenix5.WPI_TalonSRX(15)
        self.bl_motor = phoenix5.WPI_TalonSRX(18)
        self.Joystick = wpilib.Joystick(8)

        #create motor group
        self.rm = wpilib.MotorControllerGroup(self.fr_motor, self.br_motor)
        self.lm = wpilib.MotorControllerGroup(self.fl_motor, self.bl_motor)

        self.rm.setInverted(True)
        self.robotDrive = wpilib.drive.DifferentialDrive(self.lm, self.rm)

    def teleopPeriodic(self):
        self.robotDrive.arcadeDrive(-self.robotDrive.arcadeDrive(self.Joystick.getY(), self.Joystick.getX()))