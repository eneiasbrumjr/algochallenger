<?php

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;

/*
|--------------------------------------------------------------------------
| API Routes
|--------------------------------------------------------------------------
|
| Here is where you can register API routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| is assigned the "api" middleware group. Enjoy building your API!
|
*/
Route::post('login', 'AuthController@login');
Route::post('refresh', 'AuthController@refresh');

Route::group(['middleware' => ['auth:api']], function () {
    Route::get('/user', 'UserController@index');
    Route::post('/user', 'UserController@store');
    Route::post('/logout', 'AuthController@logout');
    Route::post('/working', 'WorkingController@store');
    Route::put('/working/{working}', 'WorkingController@update');
    Route::get('/working', 'WorkingController@index');
    Route::get('/working/{working}', 'WorkingController@show');
    Route::post('/working/{working}/student', 'WorkingController@addStudents');
    Route::post('/working/{working}/student/{student}', 'WorkingController@addStudent');
    Route::delete('/working/{working}/student/{student}', 'WorkingController@removeStudent');
    Route::get('/working/{working}/problem', 'ProblemController@index');
    Route::post('/working/{working}/problem', 'ProblemController@store');
    Route::get('/problem/{problem}/run', 'RunController@index');
    Route::post('/problem/{problem}/run', 'RunController@store');

    Route::get('download/problem/{problem}/zip', 'ProblemController@downloadZip');
    Route::get('download/problem/{problem}/description', 'ProblemController@downloadDescription');
    Route::get('download/run/{run}/file', 'RunController@downloadFile');


});
