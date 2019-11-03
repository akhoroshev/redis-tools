#!/usr/bin/python3

import datetime
import os

import pandas as pd
from graph_testing import test_performance_on_suite
from argparse import ArgumentParser


RDF_GRAMMARS_PATH = '/home/jblab/CFPQ-with-RedisGraph/CFPQ_Data/data/graphs/RDF/Grammars'
WS_GRAMMAR_PATH = '/home/jblab/CFPQ-with-RedisGraph/CFPQ_Data/data/graphs/WorstCase/Grammars/Brackets.txt'
# SF_GRAMMAR_PATH = '/home/jblab/CFPQ-with-RedisGraph/redis-rdf/src/graph_gen/grammars/an_bm_cm_dn.txt'
SF_GRAMMAR_PATH = '/home/simleton/Repo/redis-rdf/src/graph_gen/grammars/an_bm_cm_dn.txt'

NEO4J = [
    # ('geospeices.txt', f'{RDF_GRAMMARS_PATH}/geo.cnf'),
    ('directed_free_scale_net_500_1.txt',  SF_GRAMMAR_PATH),
    ('directed_free_scale_net_500_3.txt',  SF_GRAMMAR_PATH),
    ('directed_free_scale_net_500_5.txt',  SF_GRAMMAR_PATH),
    ('directed_free_scale_net_500_10.txt',  SF_GRAMMAR_PATH),
]

RDF = [
    ('go.txt', f'{RDF_GRAMMARS_PATH}/GPPerf1_cnf.txt'),
    ('go-hierarchy.txt', f'{RDF_GRAMMARS_PATH}/GPPerf1_cnf.txt'),
    ('eclass_514en.txt', f'{RDF_GRAMMARS_PATH}/GPPerf1_cnf.txt'),
    ('enzyme.txt', f'{RDF_GRAMMARS_PATH}/GPPerf1_cnf.txt'),
    ('atom-primitive.txt', f'{RDF_GRAMMARS_PATH}/GPPerf1_cnf.txt'),
    ('funding.txt', f'{RDF_GRAMMARS_PATH}/GPPerf1_cnf.txt'),
    ('people_pets.txt', f'{RDF_GRAMMARS_PATH}/GPPerf1_cnf.txt'),
    ('wine.txt', f'{RDF_GRAMMARS_PATH}/GPPerf1_cnf.txt'),
    ('biomedical-mesure-primitive.txt', f'{RDF_GRAMMARS_PATH}/GPPerf1_cnf.txt'),
    ('generations.txt', f'{RDF_GRAMMARS_PATH}/GPPerf1_cnf.txt'),
    ('pizza.txt', f'{RDF_GRAMMARS_PATH}/GPPerf1_cnf.txt'),
    ('travel.txt', f'{RDF_GRAMMARS_PATH}/GPPerf1_cnf.txt'),
    ('core.txt', f'{RDF_GRAMMARS_PATH}/GPPerf1_cnf.txt'),
    ('foaf.txt', f'{RDF_GRAMMARS_PATH}/GPPerf1_cnf.txt'),
    ('pathways.txt', f'{RDF_GRAMMARS_PATH}/GPPerf1_cnf.txt'),
    ('skos.txt', f'{RDF_GRAMMARS_PATH}/GPPerf1_cnf.txt'),
    ('univ-bench.txt', f'{RDF_GRAMMARS_PATH}/GPPerf1_cnf.txt'),
]

WORSTCASE = [
    ('worstcase_4.txt', WS_GRAMMAR_PATH),
    ('worstcase_8.txt', WS_GRAMMAR_PATH),
    ('worstcase_16.txt', WS_GRAMMAR_PATH),
    ('worstcase_32.txt', WS_GRAMMAR_PATH),
    ('worstcase_64.txt', WS_GRAMMAR_PATH),
    ('worstcase_128.txt', WS_GRAMMAR_PATH),
    ('worstcase_256.txt', WS_GRAMMAR_PATH),
    ('worstcase_512.txt', WS_GRAMMAR_PATH),
]

FULL = [
    *NEO4J,
    *RDF,
    *WORSTCASE
]


def main():
    parser = ArgumentParser('Launch tests query suits')

    parser.add_argument('test_suite', help='name of test suite', choices=['NEO4J', 'RDF', 'WORSTCASE', 'FULL'], default='FULL')
    parser.add_argument('--host', help='redis host name', default='localhost')
    parser.add_argument('--port', help='redis port', default=6379)
    parser.add_argument('--out', help='response output dir path', default='results')

    args = parser.parse_args()
    suite = globals()[args.test_suite]

    results = test_performance_on_suite(suite)
    results_df = pd.DataFrame(results)

    now = datetime.datetime.now().strftime('%Y-%m-%d_%H:%M')

    path_result = f'results/{args.test_suite}'
    if not os.path.isdir(path_result):
        os.mkdir(path_result)
    results_df.to_csv(f'{path_result}/{now}.csv')


if __name__ == '__main__':
    main()
