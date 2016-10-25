import unittest
import fun_bd


class TestStringMethods(unittest.TestCase):

	def test_devuelve_clasificacion(self):
		clasi=fun_bd.selectClasificacion()
		self.assertEquals(clasi, fun_bd.selectClasificacion())

	def test_devuelve_marcador(self):
		marc=fun_bd.selectMarcador()
		self.assertEquals(marc, fun_bd.selectMarcador())

	def test_devuelve_local(self):
		local=fun_bd.selectResultados()
		self.assertEquals(local, fun_bd.selectResultados())

	def test_devuelve_visit(self):
		visit=fun_bd.selectVisitante()
		self.assertEquals(visit, fun_bd.selectVisitante())

if __name__ == '__main__':
   unittest.main()
