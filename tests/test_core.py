from judgeprobe.core import Pair,audit,length_preferring_judge

def test_position_bias_detected_on_equal_answers():
    r=audit(length_preferring_judge,[Pair('q','same','same')])
    assert r.position_flip_rate==1.0

def test_length_preference_is_swap_consistent():
    r=audit(length_preferring_judge,[Pair('q','long answer here','short')])
    assert r.position_flip_rate==0.0


def test_wilson_interval_contains_rate():
    from judgeprobe.core import wilson_interval
    lo,hi=wilson_interval(50,100); assert lo<.5<hi

def test_length_preference_metric():
    from judgeprobe.core import length_preference
    pairs=[Pair('q','a much longer answer','short')]
    assert length_preference(length_preferring_judge,pairs)==1.0
