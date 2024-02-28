import wpilib
import wpilib.drive
import phoenix5

class Drivetrain:
    fr_motor: phoenix5.WPI_TalonSRX
    fl_motor: phoenix5.WPI_TalonSRX
    br_motor: phoenix5.WPI_TalonSRX
    bl_motor: phoenix5.WPI_TalonSRX 

    def setup(self):
        self.rm = wpilib.MotorControllerGroup(
            self.fr_motor, self.br_motor
        )

        self.lm = wpilib.MotorControllerGroup(
            self.fl_motor, self.bl_motor
        )

        self.rD = wpilib.drive.DifferentialDrive(
            self.lm, self.rm
        )

        self.timer = wpilib.Timer()

    def arcadeDrive(self, forward, turn):
        self.forward = forward
        self.turn = turn

    def execute(self):
        self.rD.arcadeDrive(self.forward, self.turn)