@extends('layouts.app')

@section('content')
<div class="container">
    <div class="row justify-content-center">
        <div class="col-md-8">
            <div class="card">
                <div class="card-header">{{ __('Login') }}</div>

            <login-component form-action="{{route('login')}}">
                {{-- {{ csrf_field() }} --}}
                </login-component>
            </div>
        </div>
    </div>
</div>
@endsection
