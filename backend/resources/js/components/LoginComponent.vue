 <template>
    <div class="card-body">
            <form method="POST" @submit="processForm">
                <!-- @csrf -->
                

                <div class="form-group row">
                    <!-- <label for="username" class="col-md-4 col-form-label text-md-right">{{ __('E-Mail Address') }}</label> -->

                    <div class="col-md-6">
                        <ul v-if="errors && errors.length">
                            <li v-for="error of errors" :key="error.message">
                            {{error.message}}
                            </li>
                        </ul>
                        <!-- {{errors}} -->
                        {{username}}
                        <!-- {{formAction}} -->
                        <input type="text" v-model="username" name="username">

                        <!-- @error('username') -->
                            <span class="invalid-feedback" role="alert">
                                <!-- <strong>{{ $message }}</strong> -->
                            </span>
                        <!-- @enderror -->
                    </div>
                </div>

                <div class="form-group row">
                    <!-- <label for="password" class="col-md-4 col-form-label text-md-right">{{ __('Password') }}</label> -->
                    <input v-model="password" name="password">


                    <div class="col-md-6">
                        <!-- <input v-model="password"> -->

                        <!-- @error('password') -->
                            <span class="invalid-feedback" role="alert">
                                <!-- <strong>{{ $message }}</strong> -->
                            </span>
                        <!-- @enderror -->
                    </div>
                </div>

                <div class="form-group row">
                    <div class="col-md-6 offset-md-4">
                        <div class="form-check">
                            <!-- <input class="form-check-input" type="checkbox" name="remember" id="remember" {{ old('remember') ? 'checked' : '' }}> -->

                            <label class="form-check-label" for="remember">
                                <!-- {{ __('Remember Me') }} -->
                            </label>
                        </div>
                    </div>
                </div>

                <div class="form-group row mb-0">
                    <div class="col-md-8 offset-md-4">
                        <button type="submit" class="btn btn-primary">
                            <!-- {{ __('Login') }} -->
                        </button>

                        <!-- @if (Route::has('password.request')) -->
                            <!-- <a class="btn btn-link" href="{{ route('password.request') }}"> -->
                                <!-- {{ __('Forgot Your Password?') }} -->
                            <!-- </a> -->
                        <!-- @endif -->
                    </div>
                </div>
            </form>
        </div>
</template>

<script>
    export default {
        mounted () {
        },
        methods: {
            processForm(e) {
                e.preventDefault();

                axios.post(this.formAction, {
                        username: this.username,
                        password: this.password
                    })
                    .then(response => {
                        window.location.reload();
                    })
                    .catch(e => {
                        this.errors.push(e)
                    })
                }
        },
        data() {
            return {
                username: "",
                password: "",
                errors: []
            }
        },
        props: {
            formAction: String,
        }
    }
</script>