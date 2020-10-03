import unittest
import pyopenms as oms

import basicqc
import utils


class MyTestCase(unittest.TestCase):

  def test_mzmlqc(self):
    """

    Returns
    -------

    """
    exp = oms.MSExperiment()
    oms.MzMLFile().load("tests/files/example.mzML", exp)
    rq = basicqc.getBasicQuality(exp)
    print(rq)
    self.assertTrue(rq.qualityMetrics[0].name == 'Spectrum acquisition metric values - MS1')
    self.assertTrue(len(rq.qualityMetrics[0].value['RT']) == 11)

  def test_mzmlqc(self):
    exp = oms.MSExperiment()
    oms.MzMLFile().load("tests/files/example.mzML", exp)
    rq = basicqc.getBasicQuality(exp)
    print(rq)
    self.assertTrue(rq.qualityMetrics[0].name == 'Spectrum acquisition metric values - MS1')
    self.assertTrue(len(rq.qualityMetrics[0].value['RT']) == 11)
    self.assertTrue(len(rq.qualityMetrics[12].value['RT']) == 2918)

  def test_idxml(self):
    pros = list()
    peps = list()
    oms.IdXMLFile().load("tests/files/MS2_spectra.idXML", pros, peps)
    self.assertTrue(len(pros) == 1)
    self.assertTrue(len(peps) == 20)

    self.assertTrue('RNPxlSearch' in pros[0].getIdentifier())

    for pepi in peps:
      if not pepi.empty():
        # TODO if not decoy and not under threshold
        psm_count = len(pepi.getHits())
        print(psm_count)
        for psm in pepi.getHits():
          print(psm.getSequence().toString())
        if pepi.getHits():
          print(pepi.getHits()[0].getSequence().toString())

    for pepi in peps:
      pid = utils.pep_native_id(pepi)
      if pepi.getHits():
        tmp = pepi.getHits()[0]  # TODO apply custom filters and also consider 'pass_threshold'
        print(pepi.getRT())
        print(tmp.getCharge())
        print(tmp.getScore())

        tw = (tmp.getSequence().getMonoWeight(0, 0) + tmp.getCharge() * oms.Constants.PROTON_MASS_U) / tmp.getCharge()
        dppm = utils.getMassDifference(tw, pepi.getMZ(), True)
        print(pepi.getRT())
        print(pepi.getMZ())
        print(dppm)
        print(utils.getMassDifference(tw, pepi.getMZ(), False))
        print(utils.getMassDifference(tw, pepi.getMZ(), False))

        print(pepi.getRT())
        print(pepi.getRT())
        print(tmp.getSequence().toString().lstrip().rstrip())
        print(tmp.getMetaValue('target_decoy').lower() == 'target')
        print(pid)


    # Iterate over all protein hits
    for hit in pros[0].getHits():
      print("Protein hit accession:", hit.getAccession())
      print("Protein hit sequence:", hit.getSequence())
      print("Protein hit score:", hit.getScore())




if __name__ == '__main__':
  unittest.main()
