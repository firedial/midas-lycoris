import React, { useState, useCallback } from 'react';
import axios from 'axios';
import { useEffect } from 'react';
import { BalanceTable } from '../component/table';

type BalanceData = {
  id: number
  amount: number
  item: string
  kind_element_id: number
  purpose_element_id: number
  place_element_id: number
  date: string
}

const BalanceList = () => {
  const [balances, setBalances] = useState<BalanceData[]>([]);

  const getBalances = useCallback(() => {
    axios.get('/api/v1/balance').then(
      response => {
        setBalances(response.data);
      }
    ).catch(() => {
      console.log('error');
    });
  }, []);

  useEffect(() => {
    getBalances();
  }, [getBalances])

  return (
    <div>
      <h2>balance</h2>
      <BalanceTable balances={balances}></BalanceTable>
    </div>
  )
}

const BalanceCreate = () => {
  const postBalance = (balance: BalanceData) => {
    axios.post('/api/v1/balance', balance).then(
    ).catch(() => {
      console.log('error');
    });
  }

  return (
    <>
      <h2>create</h2>
      <button onClick={() => postBalance({ id: 1, item: "hoge", date: "2022/9/2", amount: 335, kind_element_id: 2, purpose_element_id: 3, place_element_id: 3 })}>post</button>

    </>
  )
}

export { BalanceList, BalanceCreate };
