import math
import time


class StepCalc:

    def __init__(self, base_multiplier, num_steps, orbit_numbers):
        self.base_multiplier = int(base_multiplier)
        self.num_steps = int(num_steps)
        self.step_multiplier = StepCalc.multiplier_for_step(
            self.base_multiplier, self.num_steps)

        self.orbit_numbers = orbit_numbers
        self.orbits = []
        self.x = []
        self.y = []
        self.log = []

    @classmethod
    def generate_orbit_numbers(cls, start, end):
        return list(range(start if start % 2 else start + 1, end + 1, 2))

    @classmethod
    def calc_filename(cls, step_calc_obj, with_datestamp=True):
        multiplier = step_calc_obj.base_multiplier
        steps = step_calc_obj.num_steps
        start = step_calc_obj.orbit_numbers[0]
        end = step_calc_obj.orbit_numbers[-1]
        timestr = time.strftime(".%Y%m%d-%H%M%S") if with_datestamp else ""

        return f"{multiplier}n_{steps}-step_{start}-{end}{timestr}.svg"

    @classmethod
    def multiplier_for_step(cls, base_multiplier, steps):
        return {
            1: [0, 1, 0.5, 0.25, 0.125, 0.1875, 0.28125],
            3: [0, 3, 4.5, 6.75, 10.125, 15.1875, 22.78125, 34.171875, 51.2578125, 76.88671875, 115.3300781, 172.9951172],
            5: [0, 5, 12.5, 31.25, 78.125, 195.3125, 488.28125, 1220.703125]
        }[base_multiplier][steps]

    def _generate_orbits(self):
        self.orbits = []
        for n in self.orbit_numbers:
            orbit = [int(n)]
            for _ in range(self.num_steps):
                n = n * self.base_multiplier + 1
                while n % 2 == 0:
                    orbit.append(int(n))
                    n = n/2
                orbit.append(int(n))
            self.orbits.append(orbit)

    def _log_str(self, start, target, multiplier, addend, sc):
        angle = self._angle_of_deviation(sc, start)
        self.log.append(
            f"n:{start}\tt:{target}\tm:{multiplier}\ta:{addend} \tsc:{sc}\td:{start-sc}\tangle:{angle}"
        )

    def _angle_of_deviation(self, a, b):
        c = math.sqrt(a**2 + b**2)
        return math.acos(b/c) * (180/math.pi)

    def calc_steps(self, exponent):
        self.x = []
        self.y = []
        self._generate_orbits()
        for orbit in self.orbits:
            exp = 1
            start, target = orbit[0], orbit[-1]
            step_calc = start * self.step_multiplier
            while step_calc > target * 2**exp:
                exp = exp + 1
            addend = target * 2**exp - step_calc
            sc = (start * self.step_multiplier + addend) / 2**exponent
            self._log_str(start, target, self.step_multiplier, addend, sc)

            self.x.append(start)
            self.y.append(sc)
