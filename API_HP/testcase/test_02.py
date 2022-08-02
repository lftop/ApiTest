import allure
import pytest
from utils.Requests import Requests
from utils.CaseDealWith import CaseDealWith
from utils.Assert import Assert
caseobj = CaseDealWith(filename="hp_api_scan.yaml")


@allure.epic("Doune_Api_Test")
@allure.feature(caseobj.test_module)
@pytest.mark.skipif(caseobj.isRun is False, reason="{0}本轮测试不执行该模块".format(caseobj.test_module))
class Test02:
    @pytest.mark.parametrize('case', caseobj.test_case, ids=[data.get('title') for data in caseobj.test_case])
    def test_scan(self, case, get_cookie):
        # print(case)
        caseobj.set_headers(get_cookie)  # 设置cookie到请求头
        url, step, headers, content_type, expected_result = caseobj.test_url, caseobj.get_step(
            case), caseobj.test_headers, caseobj.content_type, caseobj.get_expected(case)
        i=1
        for steps in step:
            print("step:",steps)
            g_method=caseobj.get_method(steps)
            print("method:",g_method)
            g_paylod=caseobj.get_test_payload(steps)
            # print("payload:",g_paylod)
            with allure.step(title="Step{0}:向{1}发送{2}请求".format(i,url,g_method)):
                    re=Requests(url=url,method=g_method,headers=headers,payloads=g_paylod)
                    ac_result=re.transfer_station()
                    print("actual:",ac_result)
                    asserts = Assert(type=content_type, actual=ac_result,expected=expected_result)
                    assert asserts.route_assert()

