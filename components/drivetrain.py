import wpilib
import wpilib.drive
import phoenix5

class Drivetrain:
    fr_motor: phoenix5.WPI_TalonSRX
    fl_motor: phoenix5.WPI_TalonSRX
    br_motor: phoenix5.WPI_TalonSRX
    bl_motor: phoenix5.WPI_TalonSRX 