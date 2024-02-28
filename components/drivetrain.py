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